#!/usr/bin/env python3
"""
Create per-bot local settings for running the paper bots without Docker:
a FreqUI dashboard on 127.0.0.1 (this Mac only) with a generated login.

Writes user_data/config/local/<bot>.json and user_data/config/local/CREDENTIALS.txt.
Both are git-ignored. Existing files are kept, so logins don't change on re-run.
"""
import json
import secrets
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "user_data" / "config"
LOCAL = CONFIG / "local"
FIRST_PORT = 8081


def main() -> None:
    LOCAL.mkdir(parents=True, exist_ok=True)
    creds = LOCAL / "CREDENTIALS.txt"
    if creds.exists():
        username, password = creds.read_text().split("\n")[1].split(": ", 1)[1].split(" / ")
    else:
        username, password = "lab", secrets.token_urlsafe(18)
    lines = ["Trading Lab local dashboards (this Mac only)",
             f"login: {username} / {password}", ""]
    for i, bot in enumerate(sorted((CONFIG / "bots").glob("*.json"))):
        name = bot.stem
        port = FIRST_PORT + i
        out = LOCAL / f"{name}.json"
        if not out.exists():
            out.write_text(json.dumps({
                "db_url": f"sqlite:///user_data/db/{name}.sqlite",
                "api_server": {
                    "enabled": True,
                    "listen_ip_address": "127.0.0.1",
                    "listen_port": port,
                    "verbosity": "error",
                    "enable_openapi": False,
                    "jwt_secret_key": secrets.token_hex(32),
                    "ws_token": secrets.token_urlsafe(24),
                    "CORS_origins": [],
                    "username": username,
                    "password": password,
                },
            }, indent=2) + "\n")
            out.chmod(0o600)
        port = json.loads(out.read_text())["api_server"]["listen_port"]
        lines.append(f"{name:28s} http://127.0.0.1:{port}")
    creds.write_text("\n".join(lines) + "\n")
    creds.chmod(0o600)
    print(creds.read_text())


if __name__ == "__main__":
    main()
