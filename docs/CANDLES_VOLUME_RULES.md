# Candles & Volume Rules — الشموع والكميات

Extracted from the Telegram channel **«الـمـلـخـص ٩»** only (the user's study channel), Nov 2026.
Source references use the channel's message number (`msg N`) and, for videos, the time in the video (`@mm:ss`).

> **Status: draft 2. Slides + text, plus the spoken audio of lesson 1 (`msg 7`).** Every slide was read frame by frame.
> The user supplied a full Arabic transcript of lesson 1 (27 Nov 2026). Rules confirmed or added from what the
> presenter says are marked **`[audio]`**. The other lessons are still slides-only; their transcripts will be merged the same way.
>
> The channel has download protection, so the PDFs (`msg 9, 28, 45, 69, 70, 71, 84, 115, 117`) could not be opened.
> Several of them are shown on screen inside the short clips, and those pages are covered.

Two courses are in the channel:

| Course | Teacher (as shown on slides) | Messages |
|---|---|---|
| **A. Main course** — مناطق صناع السوق + النماذج اللحظية + الفوليوم | Ahmed Abu Abdullah (`@Ahmed_Abuabullah`) | lessons `msg 7, 26, 43, 67, 73, 76`, discussions `msg 8, 27, 44, 68, 74`, text `msg 10` |
| **B. "الدورة الاحترافية"** (forwarded) — supply/demand zones | Abu Madeleine (أبو مادلين) | short clips `msg 92–138`, lessons `msg 81, 83, 86, 88, 90, 116, 141, 142` |

The method in one sentence:
**Find a market-maker zone on a higher timeframe (daily/weekly), wait for price to come back into it, then enter only when an intraday pattern (15 m / 5 m) forms inside the zone, with a stop of at most 3 %.**

الفكرة باختصار: **حدد منطقة صناع السوق على الفاصل الأكبر (يومي/أسبوعي)، انتظر عودة السعر لها، ثم ادخل فقط عند ظهور نموذج لحظي (ربع ساعة / خمس دقائق) داخل المنطقة، بوقف خسارة لا يزيد عن ٣٪.**

---

## 1. Candle definitions — تعريف الشموع

Source: `msg 10` (text post, verbatim copy in project files), `msg 43 @9:35`.

**Change % is measured from the previous candle's CLOSE to this candle's CLOSE**, not open→close (`msg 43 @9:35`; `msg 10`: with a gap, count from the previous close).
نسبة التغير = من إغلاق الشمعة السابقة إلى إغلاق الشمعة الحالية، وليست بين افتتاح الشمعة وإغلاقها.

### 1.1 Positive candles — الشموع الإيجابية

| # | Name | Rule | Thresholds |
|---|---|---|---|
| P1 | **Buying candle** شمعة شرائية | close-to-close change ≥ threshold | 15 m: **≥ +1 %** · 1 h & daily: **≥ +3 %** · weekly: **≥ +10 %** |
| P2 | **Gap-down reversal** شمعة تفتتح بفجوة سفلية كبيرة | opens with a big gap down, and close − open ≥ the P1 threshold | same as P1 |
| P3 | **Bullish engulfing** شمعة ابتلاعية | *ideal*: low < prior low **and** high > prior high (engulfs body + wicks). *non-ideal*: engulfs prior body, provided the engulfed candle has no long **upper** wick left un-engulfed. Size does not matter. | none |
| P4 | **Close above a volume candle** شمعة الكميات إذا تم الإغلاق أعلاها | a close above the high of a volume candle (§4) | — |

### 1.2 Negative candles — الشموع السلبية
Mirror image: **selling candle** شمعة بيعية ≤ −1 % (15 m), ≤ −3 % (1 h, daily), ≤ −10 % (weekly); gap-up reversal; bearish engulfing (engulfed candle must not have a long **lower** wick left out); **close below a volume candle**.

### 1.2a The 4 negative candles as spoken in the lesson 2 discussion — `[audio]` (transcript checked against the video `msg 27`, 28 Nov 2026)
| # | Candle | Rule as spoken | Video example |
|---|---|---|---|
| N1 | **Selling candle** شمعة بيعية | daily change (previous close → close) **≤ −3 %** | 1:00, a −3.49 % day; the transcript says "7 %" here, the chart shows −3.49 % |
| N2 | **Gap-up reversal** (hollow red candle) | opens with a gap **up**, then falls; measure **open → close** (not from the previous close). If that fall is **≥ 3 %**, it is a selling candle: "a strong seller used the news to unload". Often news and high volume. | 5:00: opened 144.00, closed 136.00 (−5.6 % open→close) while its close-to-close change was **+3.50 %**. The "5 %" in the transcript is this example's size; the rule is 3 %. |
| N3 | **Bearish engulfing** | engulfs the previous candle. Ideal = engulfs body and wicks; non-ideal = body only. **Change % and volume don't matter.** "Single-decision" candle: exit **at its close**, no next candle needed. | 8:40: 27-11-2024, line drawn at the close 22.66 (a −3.49 % day too, "two things in one candle") |
| N4 | **Close below a volume candle** | a very high volume bar that comes **after a rise**; a close below its low = exit, the seller is confirmed. With a gap, measure from the previous close. | 12:00 (line 52.50); 14:00 مياهنا daily: volume candle high 45.54 / low 39.00, exit on the close below 39.00 (the transcript's "9.30") |

He stresses reading candles together («النظرة الشمولية»): one candle can be a selling candle, an engulfing and a broken volume candle at once.

### 1.3 Other candle shapes used (course B, `msg 94`; course A, `msg 43`)
- **Inside bar / harami** الأنسايد بار (الهرامي، المرأة الحامل): a mother candle with one or more candles fully inside it. *Fewer inside candles = stronger* (`msg 43 @15:35`, slide). `[audio L3]` He withdraws this: the slide is old, and in his experience the number of inside candles gives neither strength nor weakness. The mother's colour doesn't matter to him either (books say it should be red).
- **Spinning top** شمعة المغزل: two roughly equal wicks, small body. (`msg 43 @13:50`)
- **Pin bar** البين بار: long lower wick versus the body, very small or no upper wick. (`msg 43 @24:35`)
- **Marubozu** المربوزو, **Doji** الدوجي (weakest candle on its own), **Base candle** البيس (body ≤ wicks). Engulfing is called "the best candle". (`msg 94`)

---

## 2. Market-maker zones — مناطق صناع السوق

### 2.1 Where buyers (demand) sit — مناطق صناع السوق لصالح الشراء (`msg 7`, lesson 1)

`[audio]` Why it works: market makers can't hide their footprints because their size is large («لا يستطيعون إخفاء آثارهم بسبب كمياتهم العالية»).
Our job is to find those footprints and follow them. **Zones are drawn on the higher timeframe; the footprints (entry patterns) are looked for on the lower one.**

Slide list (the slides show 9 items; in the audio the presenter groups them into **7 zones**, treating "close above a volume candle" and
"close above a selling candle" as part of zones 3 and 6; see 2.1a):
1. **General uptrend** (higher highs and higher lows). `@9:48`
2. **Previous bottoms** that price rose from and has now returned to. `@11:32`
3. **Volume candles** that price rose from and has returned to: only market makers can print them. `@12:47`
4. **Prominent buying candles** that price rose from and has returned to. `@14:47`
5. **A broken (breached) top**: after the breakout, price comes back to it (retest). `@16:32`
6. **A long selling candle that was breached**: price rose above it, then came back to it. `@18:17`
7. **A close above a volume candle**: buyer superiority, even after a downtrend or a range. `@21:05`
8. **A close above a selling candle.** `@21:47`
9. **Fibonacci retracements 50 % and 61.8 %** of the prior up-move. `@22:32`

### 2.1a The 7 zones as spoken in lesson 1 — `[audio]` (transcript checked against the video, 28 Nov 2026)

Every slide in `msg 7` (24 min) was matched to the transcript: intro 0:41, five tools 1:35, two timeframes 5:05, market makers 8:53, zones 1–7 at 10:00, 11:32, 12:50, 14:50, 16:38, 18:20, 20:26 (volume, close above), 21:50 (selling candle), 22:40 (Fib), end 23:45. They agree except for the two points marked below. The two-timeframe slide lists three things the lower TF gives (entry, stop, target); the presenter adds a fourth out loud, the size of the risk.

| # | Zone | What the presenter adds out loud |
|---|---|---|
| 1 | **Uptrend** (المسار الصاعد): higher highs and higher lows | Called "the backbone" of high-probability trades. **But be careful** if price in an uptrend faces a previous resistance, a big moving average, or a supply zone. Example: buying at 86 "because the trend is up", then price fell back to 57. |
| 2 | **Previous low** that price rose from, then came back to | Mark the bottom candle's **high and low**. On the return, drop to a smaller timeframe and look for a pattern that shows the buyer is defending the zone. Example: rose 66 to 86, then came back. |
| 3 | **Volume candle** | Has **two** zones: (a) **a close above the volume candle** (positivity in the *current* zone), and (b) **a return to it after price rose from it** (the *opposite* zone). Volume bar = higher than the previous bars. **Preferably after a decline.** If there's a gap, measure from the previous close. A close above it shows the buyer is winning, and it's **stronger after a downtrend or a sideways range** (slide at 20:26 reads «بعد مسار هابط أو مسار عرضي»; the transcript's "uptrend" is a transcription slip, and it also contradicts "preferably after a decline"). "Only market makers can print volume candles. **Volume is the key to truth**" (الفوليوم مفتاح الحقيقة). Example used the weekly as the higher TF and 1 h as the lower one. |
| 4 | **Prominent buying candle** that price rose from, then came back to | Only a strong buyer can print it (example: one week from 71 to 90). **The zone runs from its low to its close, not its high**, because change % is measured on closes. On a return to it, look for a bullish pattern. |
| 5 | **Broken previous high** | A top is a seller's zone. Once price **closes above it** and rises, it becomes a buyer's zone. Mark the top's high and low. On a retest, look for a bullish pattern on the lower TF. "Only a strong buyer can break a previous high and rise after it", so expect him to defend it. Example: +48 % after the retests. |
| 6 | **Broken long selling candle**: a "price trap" (مصيدة سعرية), which he calls «انتفاء السلبية» | Logic says price should keep falling after a strong selling candle. If it **closes above the selling candle's high** instead, the negativity is cancelled and becomes a trap in favour of buyers. **The close above it is enough** to make the zone valid. A later return to it is also a buy zone. Example: a selling candle of −16 % that price closed above. Same logic as a close above a volume candle. |
| 7 | **Fibonacci 50 % / 61.8 %** | Draw the Fib on the wave with **0 at the top and 100 at the bottom**. The slide and PDF page 13 agree: **0 % at the peak (60.1) and 100 % at the bottom where the rise started (9.91)**, so the 50 % and 61.8 % levels are pullbacks of that rise. This is the same thing he says out loud (0 at the top, 100 at the bottom). Wait for price at the **50 %** or **61.8 %** level, "the most worthy levels". Then drop to a smaller TF for a bullish pattern. |

Each zone is only a *permission* to buy; **the entry always needs a bullish pattern on the lower timeframe** inside it.

### 2.2 Where sellers (supply) sit — لصالح البيع (`msg 26`, lesson 2)
Mirror of 2.1: downtrend (lower highs and lower lows) `@2:45`; previous tops `@4:45`; volume candles, selling candles and long buying candles that price fell from and has returned to; a **broken bottom** when price comes back up to it `@15:00`.

### 2.2a The 7 seller zones as spoken in lesson 2 — `[audio]` (transcript checked against the video, 28 Nov 2026)

Slides in `msg 26` (36 min): intro 1:41, zones 1–7 at 2:43, 4:43, 6:25, 8:43, 10:25, 12:25, 13:55, end 15:15 (the two key notes are spoken over it), then the intraday sell patterns 19:50–34:20. Transcript and slides agree; the transcript's two slips are noted below.

| # | Zone | What the presenter adds out loud |
|---|---|---|
| 1 | **Downtrend** (lower lows, lower highs) | Not always a sell. A positive pattern or a cancelled negative (e.g. a long selling candle that price closed above) can still give a speculative bounce: example 90 → 120. |
| 2 | **Previous tops** that price returns to | "Trapped holders" sit there. Mark the top's high and low. Price returned to it up to five times and fell each time. If you hold a long trade there, **think about selling**. |
| 3 | **Volume candle after a rise, then a close below it** | The close below is enough to make it a seller zone, and a later return to it is too. The volume owner is now trapped and will sell on a return (example: fell to 31, sells on the way back to 38.35). |
| 4 | **Volume candle after a rise with a long upper wick, then its low is broken** | The long upper wick *suggests* a strong seller; the **close below the candle confirms** it. Measure the low from the previous close if there's a gap. |
| 5 | **Broken prominent buying candle** (after a strong rise) | A close below its low cancels the positivity («انتفاء الإيجابية»), which is negative. Price often comes back to test the low, then falls. (The transcript says "volume candle" in the definition; the slide says buying candle.) |
| 6 | **Prominent selling candle** that price fell from, then returned to | Only a strong seller prints it; a return to it is a seller zone. |
| 7 | **Broken bottom** that price returns to (role reversal / retest) | Mark its high and low. On the retest, a fall is expected **if an intraday bearish pattern forms**. |

**Two key notes** (spoken at the end of part 1):
- A **demand zone** in supply/demand teaching is a market-maker *buy* zone; a **supply zone** is a *sell* zone.
- **Buy zones = positivity achieved, or negativity cancelled. Sell zones = negativity achieved, or positivity cancelled.** He asks students to memorise this.

### 2.3 Drawing the zone — رسم المناطق (course B, `msg 96`)
| Base candle | Zone from → to |
|---|---|
| Engulfing | lowest wick → **top of the body of the engulfed candle** |
| Inside bar | lowest wick → top of the body of the inside ("embryo") candle |
| Doji | low of wick → high of wick |
| Base candle | low of wick → top of body |

### 2.4 Grading the zone — تقييم المنطقة (course B, `msg 98`)
A valid zone needs all of:
- a **full candle exits** the zone;
- the move away is **≥ 2 × the zone height** (خروج ضعفين المنطقة);
- the zone is **fresh**: price is visiting it for the first time (فرش);
- **fewer than 6 candles** inside the zone.

Enhancers: the exit is made by **two** buying/selling candles; prefer a bottom that is a reversal, not a continuation.

### 2.5 When zones are valid: multi-timeframe filter — شروط اعتماد المنطقة (course B, `msg 100`)
- If the **daily** trend is up and these zones are **not broken**, take intraday trades inside the zone. These zones give the fastest targets.
- If the daily zones **are broken**, rely only on **weekly** zones.
- A zone broken on the daily means sellers are in control, and the next zones may be weekly or monthly.
- A demand zone only counts once the move from it **broke a prior top**: the buyer has to beat the sellers' zone first.

---

## 3. Entry: intraday patterns inside the zone — النماذج اللحظية

Rule (`msg 7 @5:00`, `msg 43 @2:00`): use **two timeframes**. The higher one (daily/weekly) confirms the zone is valid for buying. The **intraday** one (15 m, or 5 m) gives the pattern, the entry, the stop and the target.

`[audio]` Confirmed and detailed in lesson 1:
- **Higher timeframe, read from two perspectives** (منظورين):
  1. **The opposite zone** (المنطقة المقابلة): price is falling and reaches an old buyer's zone. That zone is valid for buying.
  2. **The current zone** (المنطقة الحالية): positivity has *formed* where price is now, e.g. a close above a volume candle or above a selling candle.
- **Lower timeframe:** look for a **technical pattern supporting a rise**. It fixes the **entry price, stop-loss, target and risk amount**. In the Saudi market only buys are possible, so only bullish patterns are used.
- **"Trade quality comes from managing the trade, not from the pattern"** (جودة الصفقات من خلال إدارتها وليس من خلال نماذجها).
- **If you can't watch the market full-time, raise the timeframe**: use 1 h instead of 5 m / 15 m.
- Stay away from distractions **10:00–15:00** (the Saudi session), and don't overuse indicators (overbought/oversold readings, crossovers). Keep it simple.
**The stop-loss distance must not exceed 3 %.** (`msg 43 @2:00`: «نسبة الخسارة التي يشترط أساسياً ألا تزيد عن ٣٪»)

Every example in lesson 3 has the higher-TF zone drawn in green and the 15 m pattern forming **inside** it.

### 3.1 The 12 buy patterns (`msg 43`, lesson 3)
| # | Pattern | Trigger (long) | Source |
|---|---|---|---|
| 1 | **Role reversal / retest** تبادل الأدوار / إعادة الاختبار | a broken top is retested from above and holds | `@4:00` |
| 2 | **False break** الكسر الوهمي | price breaks the previous intraday **low** inside the zone, then recovers above it | `@7:20` |
| 3 | **Close above a selling candle** الإغلاق أعلى شمعة بيعية | a 15 m selling candle (≤ −1 % close-to-close), then a later candle **closes above its high** | `@9:35` |
| 4 | **Close above a volume candle** الإغلاق أعلى شمعة كميات | a close above the high of the intraday volume candle | `@12:20` |
| 5 | **Spinning top** شمعة المغزل | spinning top inside the zone, then buy above it | `@13:50` |
| 6 | **Inside bar** الأنسايد بار | breakout above the mother candle's high | `@15:35` |
| 7 | **Bullish engulfing** الابتلاعية الشرائية | the engulfing candle itself. A *confirmation* candle: **no need to wait for a close above it** | `@19:20` |
| 8 | **Failed bearish engulfing** فشل الابتلاعية البيعية | a bearish engulfing forms, then a candle **closes above it** | `@22:20` |
| 9 | **Pin bar** البين بار | pin bar in the zone, buy on the confirmation candle | `@24:35` |
| 10 | **Break of a buying candle, then close above it** كسر شمعة شرائية ثم الإغلاق أعلاها | a 15 m/5 m buying candle (≥ +1 %) is broken, **even by a wick only**, then price **closes back above it** | `@27:20` |
| 11 | **Fakey** الفيكي باترن | inside bar, but price first breaks the mother's **low** (even by a wick), then **closes above the mother's high** | `@30:50` |
| 12 | **Positive divergence** الدايفرجنس الإيجابي | price makes a lower low while RSI makes a higher low. Entry on a close above the pattern | `@34:35` |

### 3.1a Lesson 3 as spoken — `[audio]` (transcript checked against the videos, 28 Nov 2026)
The transcript is two recordings joined: the **discussion video `msg 44` from 0:00 to ~20:00** (the three notes and the stock examples), then the **lesson video `msg 43` from the end of slide 6 (~18:30) to the end** (patterns 7–12). Spoken audio for slides 1–6 and for `msg 44` after 20:00 (الزامل onwards) is not in it.

**The three notes he says to "memorise like your names"** (`msg 44`, start):
1. Lesson 1's zones and the four positive candles can show up **on the same timeframe as the pattern** (e.g. a ≥ 3 % candle on 15 m). That gives the price a positive view, **not an entry**: «لا دخول إلا بنموذج لحظي داعم للصعود».
2. Every bullish pattern is one of two things: **positivity achieved, or negativity cancelled**.
3. **The most important point of the course**, his one-sentence summary: **the more bullish patterns on the chart at the same place, the stronger the setup** (النظرة الشمولية).

**Pattern details from the audio** (slide times are `msg 43`):
| # | Pattern | What the audio adds | Slide |
|---|---|---|---|
| 6 | Inside bar | Stop = the lowest point between the mother candle and the candle that closed above it. Number of inside candles and mother colour don't matter (see §1.3). | ~18:30 |
| 7 | Bullish engulfing | Ideal = engulfs body and wicks; non-ideal = body only. Volume and change % don't matter. **Single-decision**: complete at its close, no confirmation needed (every other pattern needs a close after it). The upper line belongs at its **close**; the slide puts it at the high and he calls the slide wrong. | 19:20 |
| 8 | Failed bearish engulfing | "Negativity cancelled". A bearish engulfing forms, then a candle **closes above it**. Stop = lowest point between the top of the bearish engulfing and the close above it. | 22:15 |
| 9 | Pin bar | Long lower wick versus the body, small or no upper wick, body at the top. **Colour doesn't matter.** The buyer's strength is judged by the **close above the pin bar**. "Pin bar combo" closes inside the prior candle's range; don't dwell on the difference. | 24:25 |
| 10 | Broken buying candle, then close above | «لا يوجد نموذج اسمه إغلاق أعلى شمعة شرائية»: a buying candle (15 m ≥ 1 %) must **first be broken** below its low (wick or body), **then** price closes above its high. Weakness: the stop can be large, about 3 % or more. Some traders accept price just returning inside the candle; he requires the close above. | 27:15 (slide: "≥ 1 % on 15 m or 5 m; a break even by a wick counts") |
| 11 | Fakey | **Main condition, said three times: the candle right after the mother must be inside the mother's range** (high to low incl. wicks). If the next candle breaks the mother, it is not a fakey. Then the mother's low is broken (wick or close, one or several candles), then a **close above the mother's high**. Stop = lowest point between. Mother colour doesn't matter. | 30:50 |
| 12 | Positive divergence | **Supporting evidence only (للاستئناس), not an entry pattern**: at the second bottom a candle pattern usually forms anyway. Price lower low + RSI higher low. Some traders measure it on closes (line chart) instead of wicks. | 34:20 |

**Rules spoken with the examples (`msg 44`, checked against the charts):**
- **Entry** is when the pattern completes; whether to enter at once, wait for a retest, or split the size is the trader's choice. (حرفي, 4:24–9:00)
- **Measuring**: stop % from the **upper line (the pattern line) down to the lower line**; target measured from the upper line **upwards**. (إعمار, lines 14.11 / 13.80, 9:20–11:40)
- **Gaps are ignored inside candle patterns** (e.g. the fakey). (حرفي)
- **Don't be too strict on thresholds**: a 15 m candle of **−0.96 %** was accepted as a selling candle «ولا نحجر واسعًا». (إنتاج, 06-07-2025 13:45, close 43.36, 18:40–19:50)
- **Confluence examples**:
  - حرفي: price returns to the opposite zone (a ≥ 3 % 15 m buying candle). There it makes a bullish engulfing, a false break of a prior low (gap: measure from the previous close), a fakey, and a positive divergence, all at once.
  - إعمار: a ≥ 1 % buying candle broken then closed above, plus a close above a ≥ 1 % selling candle: two patterns in one zone.
  - المطاحن العربية (12:06–13:00): an inside bar whose mother candle is also a volume candle; the stop is the lowest point between, and the target was hit.
  - سينومي ريتيل (13:10–16:30): the zone is a volume candle that is also a > 3.5 % buying candle. Inside it come a fakey, a pin bar that rose > 10 %, and later an inside bar. The mother there is a ≥ 1 % negative candle and a spinning top.
  - جبل عمر (17:00–18:10): one candle that engulfs the candle before it, is the mother of the inside bar after it, and breaks the prior bottom. Price made a lower low while RSI did not.

### 3.1b The lesson PDFs: worked numbers per pattern (`msg 9, 28, 45`, sent by the user 28 Nov 2026)
The three lesson PDFs are the same pages as the video slides (lesson 1: 15 pages, lesson 2: 10, lesson 3: 15). Every page matches §2.1, §2.2a and §3.1, with no new rules. The PDFs also confirm that seller zone 5 is a broken **buying** candle (page title «الشمعة الشرائية المكسورة التي تأتي بعد صعود»).
What they add is clean numbers for each lesson 3 example. All are 15 m patterns inside a higher-TF zone, **mostly weekly zones**:
| # | Pattern | Zone it formed in (as labelled) | Lines (entry / stop) | Stop % | Move shown |
|---|---|---|---|---|---|
| 1 | Retest | broken prior top | 65.80 / 64.20 | 2.51 % | +4.13 % |
| 2 | False break | prior **daily** bottom | 64.50 / 63.40 | 1.72 % | — |
| 3 | Close above selling candle | **weekly** volume candle price rose from, then returned | 14.32 / 14.10 | 1.56 % | — |
| 4 | Close above volume candle | **weekly** long selling candle that was breached | 22.20 / 21.70 | 2.30 % | — |
| 5 | Spinning top | **weekly** demand zone | 45.50 / 44.40 | 2.47 % | +3.58 % |
| 6 | Inside bar | prior bottom | 12.08 / 12.00 | 0.67 % | +4.98 % |
| 7 | Bullish engulfing | **weekly** breached top | 30.45 / 30.15 | 1.00 % | — |
| 8 | Failed bearish engulfing | **weekly** breached top | 91.70 / 90.30 | 1.55 % | — |
| 9 | Pin bar | **weekly** bottom | 162.40 / 157.60 | 3.00 % | — |
| 10 | Broken buying candle | **weekly** demand zone | 172.60 / 168.60 | 2.41 % | — |
| 11 | Fakey | breached long selling candle | 25.20 / 24.96 | 0.96 % | +5.77 % |
| 12 | Positive divergence | breached top | 24.48 / 24.00 | 2.02 % | — |
Every stop is **≤ 3 %**, matching the lesson 3 PDF intro: the stop «يشترط شرطاً أساسياً ألا تزيد عن ٣٪». Where a move is shown, it is about 1.5–6× the stop.

### 3.2 Course B versions of the same ideas
- **High-volume candle model** شمعة الكميات العالية (`msg 107`): *"the positive model is to break it first, then return and close above it, in an uptrend"*. In other words: price dips below the high-volume candle, then closes back above it.
- **Buying-candle break model** نموذج كسر الشمعة الشرائية (`msg 110`): buying candle → broken → close back above = positive. **Stop: under the lowest point between the broken candle and the closing candle.**
- **Selling-candle model** الشمعة البيعية (`msg 112`): a selling candle in an uptrend, then **a close above it** → buy. **Stop: below the selling candle's low.**
- **False break** = "a break of a bottom" (`msg 103`).
- **Divergence** (`msg 114`): positive at bottoms, negative at tops, RSI.

### 3.3 Sell-side patterns (`msg 26` part 2: النماذج اللحظية الداعمة للهبوط)
False breakout above the zone high, negative divergence, **shooting star** الشهاب, bearish engulfing, doji, break of a buying candle, break of a volume candle. Example: a 15 m false breakout inside a zone made by a broken volume candle that price came back up to. (`msg 26 @19:00–25:00`)

**`[audio]` lesson 2, part 2: the six intraday bearish patterns (15 m / 5 m), each inside a higher-TF seller zone**
| Pattern | Rule as spoken | Slide |
|---|---|---|
| **False breakout** الاختراق الوهمي | A previous top is broken, even by a wick. Draw a line at the **low of the candle that broke it**; a **close below** that line completes the pattern. | 19:50, zone = broken volume candle |
| **Negative divergence** | Price makes a higher (or equal) top while **RSI(14)** makes a lower or equal top. Line at the **low of the second-top candle**; a close below completes it. Watch for it when tops are close together. | 22:30 (5 m) |
| **Shooting star** | Mostly a long upper wick, small body at the bottom. Mark its high and low; a **close below** it completes it. | 25:25 |
| **Bearish engulfing** | Lines at its high and its **close** (the slide's lower line at the low is wrong, he says). Single-decision candle: act **at its close**, don't wait for a close below. | 27:55 |
| **Doji** at a broken bottom | Body small versus the wicks. Close below it completes it. | 30:30 |
| **Broken buying candle** | 15 m buying candle = **≥ 1 %**, measured from the previous close (here the auction close). A close below its low in a seller zone → exit. | 32:15 |
| **Broken volume candle** at a prior top | Measure from the previous close (gap at the auction). A close below → exit. With a news gap-up and high volume, the exit line is the **low of the candle's body**. | 34:20 |

**`[audio]` lesson 2 discussion (`msg 27`), exit examples on 15 m (checked against the video)**
- **Look for exit patterns at the highest prices**: they formed there, which is why price fell after. (17:00)
- **One close, three exit signals** (أديس, 15 m, ~18:00): a **≥ 1 % buying candle** that is also a **very high volume candle**, at a second top with a **negative divergence**. The close below that candle's low (line 13.70) cancels the buying candle, breaks the volume candle and completes the divergence (close below the low of the second-top candle). An experienced trader sees the divergence from close tops without opening RSI.
- **False breakout + bearish engulfing** (علم, 15 m, 19:05): candle at 10:15 on 30-04-2025, change only −0.34 %, exit at its close 1014.50. **Auction candles count for nothing**, as if they weren't on the chart. Some traders call that candle a spinning top or doji and wait for a close below its low instead.
- **Early exit or confirmed exit is the trader's choice** (الأندلس, 15 m, 21:10): a bearish engulfing (close line 22.42) next to a volume candle (low 22.30), 12 halalas apart. Exit at the engulfing's close, or wait for a close below the volume-candle low.
- **Review** (مياهنا, 23:40): the daily seller zone is a prior top that is also a broken volume candle, drawn from the **previous close (24.86) to the high (27.30)**; "don't draw it wide". On 15 m inside it: a ≥ 1 % buying candle with very high volume, close below its low (26.88) → exit.
- **Q&A:**
  - After price breaks below a selling candle, a retest is **not** required. If price does come back to it, it's a seller zone; raise your caution. The transcript says "only a strong **buyer** forms it", but he means seller (he said strong seller earlier).
  - Marking a volume candle on the higher timeframe: mark its high and low on the daily, then when price returns go to 15 m (sometimes 5 m) and wait for a bearish pattern. (28:00, مياهنا 45.54 / 39.00)
  - "The bottom of the selling candle" is an advanced topic, left for later.


---

## 4. Volume — الفوليوم مفتاح الحقيقة (`msg 67`, lesson 4)

- Volume = shares traded (buys + sells) **on the same timeframe** as the chart. `@4:00`
- 5 levels of volume bar (very high, high, medium, low, very low). **The colour of the volume bar does not matter.** `@4:30–7:30`
- Volume candles are **makers' candles**: never random, and you must find their **cause**. `@8:15`, `@14:20`
- **Volume candle (working definition):** the highest-volume candle compared with the candles before it («أعلى شمعة كميات مقارنة بما قبلها»). `@11:40` *(No exact multiplier is given on the slides. To be confirmed in the audio pass.)*

**Where volume candles appear** (مواقع تكون الفوليوم, `@9:20–13:00`):
- after a rise, with **no close above** it → a seller met the buyer;
- after a rise, with a **close above** it → buyer superiority, the move continues;
- after a fall, with **no close above** it.

**Why they form** (أسباب, `@16:00–24:00`): price reached an opposing level, such as
the top of a long selling candle (higher or same TF), the top of a volume candle (higher or same TF), the **low of a higher-TF volume candle** (example: a 15 m volume spike when price reaches a weekly volume candle's low), a breakout through the low of a broken volume candle, the top of a broken buying candle, or a previous top.

**Strategies** (خلفيات واستراتيجيات التداول على الفوليوم, `@28:00–33:00`):
1. Price **above a higher-TF volume candle** → buyers dominate; look for any intraday pattern.
   Example strategy: **entry = a 15 m close above the volume candle; stop = the lowest price between the volume candle's top and the close that broke it.**
2. Price **returns to a higher-TF volume candle it rose from** (a buyer zone) → look for an intraday pattern (example: positive divergence + inside bar + a negative candle closed above).
3. Price **trades inside a higher-TF volume candle** → its **low is support** (look for entries near it) and its **high is resistance**.

---

## 5. Risk, stop and target — إدارة الصفقة

- **Stop ≤ 3 %** from entry (`msg 43 @2:00`).
- Stop placement used in the examples: under the pattern's low, under the selling candle's low (`msg 112`), or under the lowest point between the broken candle and the close-back candle (`msg 110`, `msg 67 @28:00`).
- **Target:** the slides don't give a fixed rule. The examples measure +3 % to +8 % moves to the next opposing zone (supply / previous top), e.g. `msg 43 @7:20` +7.6 %, `@15:35` +4.9 %, `@30:50` +5.7 %. *Confirmed in the practice group (§8.7): target = 2–3× the stop, exits on intraday negative patterns, stop = lowest low between the pattern line and the close above it.*
- Timeframes used: weekly/daily for zones, **15 m** (sometimes 5 m) for entries. Market in all examples: **Saudi stocks (Tadawul)**, TickerChart.

---

## 6. Codable spec (for the backtest) — draft

```
HTF = 1d (zones; also 1w)       LTF = 15m (entries)
change(c) = close[c] / close[c-1] - 1
buying_candle(LTF)  = change >= +1%     selling_candle(LTF) = change <= -1%
buying_candle(1h/1d) = change >= +3%    buying_candle(1w) = change >= +10%
volume_candle = volume >= max(volume[-N..-1])     # N to tune; "highest vs prior candles"

DEMAND ZONE on HTF (any of):
  - bullish engulfing / inside bar / doji / base candle whose exit move >= 2x zone height,
    exit by a full candle, < 6 candles in zone, zone untested (fresh), and the move broke a prior high
  [audio, lesson 1 - the 7 zones]
  1 uptrend (HH/HL) AND price not at prior resistance / big MA / supply zone
  2 return to a prior bottom candle [low, high]
  3 volume candle: (a) HTF close > its high  -> "current zone" positive
                   (b) return to [low, high] after a rise from it -> "opposite zone"
                   prefer after a decline; gap -> measure from prior close
  4 return to a prominent buying candle: zone = [low, CLOSE] (not high)
  5 retest of a broken prior high [top candle low, high] after a close above it
  6 close > high of a long selling candle (price trap), or a later return to it
  7 Fib on the wave, 0 at top / 100 at bottom: price at the 50% or 61.8% level
FILTER: daily trend up (higher highs/lows) and daily zones not broken; else only weekly zones

ENTRY (LTF, while price is inside the HTF zone), any of:
  close > high of a recent selling candle            (3.1 #3, msg 112)
  close > high of a recent volume candle             (3.1 #4, msg 67)
  low < prior swing low, then close > that low       (false break, #2)
  bullish engulfing                                  (#7, no extra confirmation)
  fakey: break of mother low, then close > mother high (#11)
  buying candle broken (even by wick), then close > its high (#10)
  inside-bar breakout, pin bar, RSI positive divergence (#6, #9, #12)
STOP: below pattern low;  reject trade if stop distance > 3%
  [group] stop triggers on a 15m CLOSE below the pattern low (not a wick); if a candle breaks it,
          mark that candle's low and exit only on a close below it (false-break filter, g#25823)
  [group] trail: move stop up under each new bullish pattern / volume candle on the LTF
  [group] skip auction volume bars when picking the volume candle (g#25123)
  [group] pick stop: prior low if within 3%, else pattern low; a >3% adverse move = failed (g#20465-67)
  [group] profit trailing: at target area drop to 5m, trail under each new positive/volume candle,
          exit on a 5m bearish engulfing (g#21970-81)
  [group] skip a bullish engulfing if negative divergence or the opposite zone is supply (g#22441-45)
  [group] quality filters to test: positive RSI divergence at entry; stock above MA200 on 15m;
          market (TASI) not in a negative pattern
  [group] market-scaled exits: good market -> sell 1/2 or 1/4 at +3%, then 1/4 per +2%;
          bad market (TASI negative) -> take +1..1.5% or skip trades / size ~5% (g#15776-87)
  [group] gap-up open: limit buy at the gap candle's lower wick, stop below it (g#17478)
  [group] zone touched many times = weaker; a pattern must complete in the zone, else wait (g#17014, 16037)
  [group] skip LTF false-break entries when HTF candles show bearish engulfing (g#16455)
  [group] STOP (teacher's definition) = lowest low between the pattern's line and the candle that
          closed above it; must be <= 3%; failure only on a close below it (g#2137, 2697)
  [group] entry = close above the pattern line; engulfing = enter at its own close (g#2296)
  [group] news gap-up + high volume: exit on a close below the candle body low (g#3221)
  [group] Mod gap-up strategy: limit buy at the gap candle's low on the first return, stop = close
          below it, target +2-3% (g#7147)
  [group] Mod volume-MA strategy: vol > SMA(vol,20) on a green LTF candle inside an HTF demand zone,
          enter on a close above its high; next qualifying candle moves the line (g#10561, 10751)
  [group] daily screener: EMA7>EMA14>EMA20>EMA35>EMA50, close>EMA7, RSI14>=50, ROC12>=0 (g#13186)
  [group] time stop: exit after 3 trading days with neither stop nor target hit (g#10822)
  [group] market quality: first-hour traded value vs recent days (teacher: ~1bn SAR) (g#3872)
  [audio L2] EXIT (long) on the LTF when inside an HTF seller zone (prior top, volume candle closed below
          after a rise, broken buying candle, broken bottom retest) and any of: close below the low of the
          candle that broke the prior top (false breakout); negative RSI(14) divergence + close below the
          second-top candle's low; close below a shooting star / doji; bearish engulfing at its close;
          close below a >=1% buying candle or below a volume candle
  [audio L2 disc] HTF negative candle (any): change <= -3%; gap-up open with (open-close)/open >= 3%
          (even if close-to-close is positive); bearish engulfing (any size/volume, decided at its close);
          close below the low of a volume candle that came after a rise. Ignore auction candles.
          Exit timing is a parameter: early = engulfing close; confirmed = close below nearby volume-candle low.
          HTF seller zone from a volume candle / prior top = [previous close, high]; no retest needed after
          a selling candle breaks, but a return to it is a seller zone.
  [audio L3] CONFLUENCE: score = number of bullish patterns completing in the same zone/bar cluster;
          "more patterns = stronger" (his key point). HTF-type candles on the LTF are context, not an entry.
          FAKEY requires bar[mother+1] inside mother's range; then low < mother.low; then close > mother.high.
          INSIDE BAR: inside-candle count and mother colour are not used. PIN BAR colour not used.
          BROKEN BUYING CANDLE: low broken first (wick ok), then close > its high; skip if stop > 3%.
          FAILED BEARISH ENGULFING: close > its high; stop = lowest low between its top and that close.
          DIVERGENCE (RSI14): filter/score only, never an entry by itself.
          Thresholds: allow a small tolerance (a -0.96% 15m candle counted as selling); ignore gaps in candle patterns.
          Stop % = (pattern line - stop line) / pattern line; target measured up from the pattern line.
  [PDF L3] HTF for zones in the worked examples is mostly WEEKLY (9 of 12), daily in one; test 1w zones, not only 1d.
TARGET (group): 2-3x the stop distance (g#4353); next supply / top
TARGET: next HTF supply zone / previous top (no fixed % in slides)
```

---

### 6.1 Design notes from the user's lesson summaries (28 Nov 2026)
These are the user's design choices for TradingLab, not course rules.
- **Principle:** don't turn a descriptive rule into a number by our own assumption. A number the course doesn't give is a labelled, tunable **parameter**.
- **Pipeline** (lesson 1 summary): Market Scanner → Zone Detection (HTF) → Zone Validation → Entry Signal (LTF) → Risk Management → Execution.
- **Zone State Engine** (lesson 2 summary): a zone is not permanently positive or negative. Track its state over time. *Positivity achieved* and *negativity cancelled* support a rise; *negativity achieved* and *positivity cancelled* support a fall. Example: a buying candle is positive until a close below it, then its positivity is cancelled.
- **Pattern lifecycle:** `Detected` (shape found) → `Pending` (waiting for the confirming close) → `Confirmed` → `Invalidated`. Engulfing candles go straight to `Confirmed` at their own close; the other patterns need a later close past their line.
- **Pattern IDs:** bearish `BEAR_01` false breakout, `BEAR_02` negative divergence, `BEAR_03` shooting star, `BEAR_04` bearish engulfing, `BEAR_05` doji, `BEAR_06` broken buying candle, `BEAR_07` broken volume candle. The bullish 12 of §3.1 can follow as `BULL_01`–`BULL_12`.
- **Confluence:** log **every** signal that completes on a bar (one candle can carry several). Don't give signals weights or confidence scores until the backtest shows whether confluence helps. This refines the [audio L3] confluence line above: record the count and test it, don't assume it.
- **Exit policy as a parameter:** early (engulfing close) versus confirmed (close below a nearby volume-candle low). Test both.

Still open in the course, with what we have so far:
| Item | Status |
|---|---|
| RSI setting | **RSI(14)** on the course slides (lesson 2 slide 22:30, lesson 3 slide 12) |
| Volume candle, numeric | none from the teacher ("higher than the bars before it"). Mod's own strategy uses vol > SMA(vol, 20) (`g#10561`). The lookback is a parameter. |
| Wick/body ratios (shooting star, doji, pin bar, spinning top) | not given; parameters |
| How close two tops must be for a divergence | not given ("close together"); parameter |
| Zone invalidation | partial: a zone touched many times is weaker (`g#17014`); if daily zones are broken, use weekly only (§3.1 filter) |
| Gap-up entry, exit on a close below the body low | Mod's gap-up strategy (`g#7147`, `g#3221`), see §6 |

## 7. Gaps — what's still missing

- **Spoken content**: lessons 1 and 2 (`msg 7, 26`) are done `[audio]`, checked against the videos; lesson 3 is done for slides 6–12 (`msg 43` from ~18:30). Still missing: lesson 3 slides 1–5, lessons 4–5 (`msg 67, 73`), the discussion videos (`msg 8, 68, 74`, and `msg 44` after 20:00; `msg 27` and `msg 44` 0–20:00 done `[audio]`; lesson 1 says the discussion «لا تقل أهمية» than the lesson), the live session (`msg 76`), and course B's long lessons. The user is supplying transcripts.
- Exact volume-candle threshold, exit/target rule, and position sizing: not on any slide.
- PDFs: download-protected.
- Lesson 5 (`msg 73`, screen design) is a TickerChart setup walkthrough: no trading rules on screen.

---

## 8. Practice group: answers from "Mod" and the teacher — `[group]`

Source: the discussion group **«احتراف المضاربات اللحظية ٩»**, where students apply what the channel teaches.
Two accounts matter: **"Mod ."** (Abu Khalid, `@modee_14`, the most active member)
and **the teacher himself, "أحمد ( أبو عبدالله )"** (`@Ahmed_Abuabullah`). References are group message numbers (`g#N`).
Coverage: **the whole group, 30 Jun 2025 – 27 Nov 2026** (messages `g#2–26794`).
Most of Mod's posts are chart images captioned with a stock name and a pattern name. Only the text is captured here.

### 8.1 Rules confirmed or added by the teacher
- **Price trap** (المصيدة السعرية) = a negative pattern that fails, or a positive pattern that is broken, **then price closes back above it**. `g#23568`
- **How to raise trade quality**: a strong zone on the higher TF, then a bullish pattern, ideally with **positive RSI divergence**, plus a good market, plus trade management. **Enter in batches**, not all at once. Focus on **momentum (speculative) stocks**. Quality over quantity. Split the portfolio between intraday trades and daily-TF trades. He himself uses no indicators. `g#24328`
- Where the method works best: a **speculative stock trading above the 200 MA on the 15 m chart**, where several setups line up at once. `g#25237`
- **Ignore an extremely high volume bar if it's the closing-auction bar** (بار كميات مزاد). `g#25123`
- **Avoiding false stop-outs** (تلافي كسور الوقف الخداعية): when a candle breaks the stop level, mark **that candle's low**. The stop only triggers on a **close below that low**. Example: an inside bar broke, the low of the breaking candle was treated as the final failure point, and the stock then made +8 %. `g#25823, 25826`
- **Exit / bearish side**: a **bearish engulfing at the highs, on its close** is an exit signal, so don't wait for a close below its low. A **shooting star after a rise, followed by a close below it** is a bearish intraday pattern. Price reaching the low of a broken buying candle (resistance) means either wait for a bearish pattern or exit. `g#25127, 25130, 25143, 25158`
- A long negative candle whose **low holds** is a recurring "technical state", not a pure pattern, and is **high risk**. `g#25141`
- Candles and volume "work in every market and every timeframe". His example was a US stock on 5 m, entered on a close above a volume candle. `g#25221–25223`

### 8.2 Mod's practical rules (stops, entries, management)
- **The default stop is the pattern stop on 15 m** (وقف النموذج ربع ساعه): exit on a 15 m **close** below the pattern low. A volume-candle entry uses the volume candle's low as the stop, on 15 m. `g#22946, 23744, 24245, 25007`
- An alternative is a wider stop at the **pattern low or the daily low / zone low**. Some traders use the bottom the move started from, if it's within about 3 % of the pattern's completion point. `g#23385, 23469, 23989`
- **Never take a trade whose stop is ~9 % away**, e.g. right after a 9 % selling candle. Wait for price to come back near the prior candle's close, which gives a tight stop. That example then made ~6 %. `g#23498–23501`
- Candles with a **long lower wick usually get revisited** down to their low or middle. `g#23505`
- **Gap setups**: the correct stop is the gap, which is far and costly. Mod's "aggressive" version uses a stop near the entry price. `g#24471–24472`
- **Trailing**: raise the stop each time a new bullish pattern forms (e.g. a bullish engulfing or a new volume candle). Use an hourly line to protect open profit. If the next resistance is farther than the speculative target, trail toward it. Otherwise take **1–3 %** and leave. `g#23860, 24155, 24512, 25067`
- **Positive divergence at a false break** is the strongest confirmation he cites. In his words, spotting the fake break was "one of the greatest things we learned in the course". `g#24165, 24523, 25229–25231`
- **Demand zones need their own management** because the stop is far. A speculator should drop to a small TF and wait for a pattern with a close stop, or accept the wide stop with a **~1 : 3 risk : reward** (risk 1,000 to make 3,000, so one win covers three losses). `g#25501, 25506`
- **A bearish engulfing cancels the setup until price closes back above it.** "Positivity" returns only with a close above the bearish engulfing, or when price falls into the demand zone and holds. `g#25433–25437, 25533`
- **A buying candle gets broken, then price closes above the breaking candle**: enter, with the stop at the lowest point of the pattern. `g#25521`
- **No decline happens without a bearish pattern forming first.** A pullback in an uptrend is a re-buy; a rally in a downtrend is a selling chance. **Always buy in buyers' zones.** `g#25936, 26354, 26369`
- **Market filter**: avoid trading when the market is negative, or trade small. Stocks that jump in the closing auction usually calm down at the next open. Watch stocks sitting at demand zones together with TASI, because when TASI rebounds they bounce first. `g#25327, 25345, 25469, 26640`
- Spread capital over about **3 stocks and trail the stop**, rather than jumping in and out. `g#26491`

### 8.3 Mod's "momentum pullback" strategy (posted 14 Nov 2026) — «الاستراتيجية»
Mod's own simpler version of a "beautiful but complicated" momentum strategy. In late Nov he applies it to TASI and to individual stocks (`g#26640, 26657, 26779–26794`).
1. Put a **50-period moving average on volume**.
2. Find a stock that **rose at least 12 % in 3 to 7 candles**, with volume bars **breaking out above the volume MA**.
3. Wait for a **pullback that forms an "M"-like shape** (a rise, a dip, a smaller rise, a dip). The two halves don't need to be equal.
4. **Enter when the buyer appears**: a buying candle with volume on the daily. You can enter earlier on **30 m** if a bullish pattern forms there. Strengthen the trade with positive divergence, a Fib level (38.2 / 50 / 61.8), or a moving average.
5. The more candles and % in the first rise, the longer the pullback takes. The fewer, the faster the next leg.
`g#26578–26614`

### 8.4 More from Mar – Jun 2026
**Teacher**
- **Profit-stop trailing technique** (فنيات رفع الوقف الربحي): once price reaches a target area (e.g. the top of a volume candle on 15 m), **drop one timeframe (to 5 m)**. Move the stop up step by step to the low of each new positive candle: engulfing, then the last positive candle, then the last volume candle, then a doji. A 5 m bearish engulfing then ends the trade. `g#21970–21981`
- **When a bullish engulfing should NOT be taken**: (1) **negative divergence** is present, or (2) the *opposite zone* is a seller's zone, e.g. a previous top that is also a broken volume candle with a bearish engulfing at the same level. `g#22441–22445`
- **Stop choice**: the pattern-failure point can be the low of the buying candle or the low of the volume candle. **Both are fine as long as each is under 3 %.** `g#22105`
- When a nearer selling candle hasn't been closed above yet, some enter on the first close, some wait for the second, and he prefers **splitting the position between the two**. `g#22099`
- **The first target of a long negative candle setup is that candle's high.** `g#22101`
- The zone can be drawn on the **same timeframe** as the entry pattern. `g#21979`
- "Don't chase" is not a rule here. A stock already up can still be a valid setup if the pattern is there. `g#21778`
- **How to test your strategy**: look at the day's top gainers. If you had flagged most of them beforehand, the strategy works. `g#21784`
- With equal or near-equal bottoms, look for positive divergence. `g#22201`
- A selling candle after a gap is measured from the **previous close**. `g#20023`
- **Scaling in** inside the pattern keeps the average loss under 3 % even when price dips. `g#20469`

**Mod**
- **Pick the stop by distance**: if the pattern stop is under 3 % and the prior low is close, use the prior low. Otherwise use the pattern stop. The teacher agreed: "that's the correct one". `g#20455–20466`
- **A drop of more than 3 % = the pattern failed**, even if there's divergence. `g#20467`
- **A positive pattern that is broken and then recovered is a trap, and the rise afterwards is fast.** `g#20468`
- **If the candle that broke the stop is itself broken, the bullish pattern has failed.** If the stop was broken only by a wick, move the stop to that wick. `g#19939, 20311, 20359`
- **A volume candle that price fails to close above means the buyer couldn't beat the seller, so expect a drop.** `g#19766–19767`
- **Draw a falling trendline on the last two lower highs.** `g#19578`
- **Fixed-risk money management**: risk 100 to make 300. Three losses (−300) are erased by one win. With two wins and two losses you're +400. You'd need four losers per winner to only break even. `g#19835–19838, 20555`
- **"Selling-candle strategy" on the intraday chart**, after a daily close above a selling candle: mark the opposite-colour candle that formed before the breakout, and the low the move started from. Selling pressure shows as upper wicks, and the trigger is a close above them. `g#20697–20704`
- **Stochastic on the hourly** (Mod's own add-on): crossing up from 20 = a rebound in rising stocks; crossing down from 80 = exit. It's not part of the teacher's method. `g#21859`
- **Always place the stop order as soon as you open the trade.** `g#21671`

### 8.5 More from Jan – Mar 2026
**Taking profit in parts** (Mod, `g#18207–18227, 18472`). This is how he actually exits:
- Sell part of the position at **+2 to 3 %**, where the first target is often the **Fib 61.8 % level**. Raise the stop to the entry price or to the last higher low.
- Sell the same amount at each further +2 %, raising the stop each time. Keep the rest until a negative pattern appears.
- If price pulls back to the stop and forms a new bullish pattern, **buy back the part you sold**.
- The simpler alternative is to sell everything at +2 to 3 % and look for the next trade.

**Position-trading on higher timeframes** (Mod, `g#17599–17609, 19220–19222`): pick **3 stocks at strong demand zones** and put an equal amount in each. Set the target at **2–3× the stop** (e.g. stop 1,000, target 2,000–3,000). Two losers and one winner still leave you up. Don't put large money into one stock.

**Demand / supply zones** (Mod, `g#18944–18947`):
- A demand zone forms at a **bottom**, or where price **breaks out of a supply zone**.
- The best demand zone is a bottom where the rise afterwards was strong and **broke a prior high**.
- When a demand zone breaks, the top of the candle that broke it becomes supply. If that supply is later broken, it becomes demand again.

**Market filter** (Mod and teacher, `g#18487, 18775, 19109–19114, 17984`):
- **Stop opening trades when TASI is at a weekly supply zone.** Trade when TASI *and* the stock are both at demand zones; that's when most patterns work.
- When TASI presses down, patterns fail more often, even at good zones.
- You don't need a trade every day. If TASI is turning down, trade small or not at all.

**Other**
- **A close at a hollow candle is usually followed by a drop back to its low.** `g#19184`
- **On news days**, check where the stock is on the chart. A gap-up on news at a top often turns into a sharp drop. `g#18685–18686`
- **Hourly "price explosion"**: mark the hourly explosion candle and wait for price to come back to it. Patterns usually form on the smaller TF first. `g#18519–18525`
- For TASI or any stock far from its moving average, draw the Fib from top to bottom (teacher). `g#18608`
- **A speculator exits as soon as a negative pattern forms on the intraday chart**, without waiting for the daily. `g#18562`

### 8.6 More from Nov 2025 – Jan 2026
**Profit-taking depends on the market** (Mod, `g#14742–14744, 15778–15787, 17385–17386`):
- **Good market**: first target **+3 % on half or a quarter** of the position, then sell another quarter at each further +2 %. The total can pass +5 %.
- **Bad market** (TASI breaking yearly lows): **+1 to 1.5 % is a good result**; selling everything at +1 % is fine.
- Hold a winner with a **raised stop** instead of hopping between stocks; you may buy the same stock back later at a higher price.

**Sizing and stops in a bad market** (Mod, `g#15773–15776, 14780–14782, 17141`):
- **Never enter without a stop**, and know it before you enter. A 3 % stop beats waiting through a 10 % drop.
- If TASI is negative, **don't trade at all** until it proves otherwise. If you must, use **about 5 % of the portfolio**. Mod himself opened no trades for over a month in a falling market.
- In a good, rising market, with all higher TFs positive, he may give a broken stop **up to 3 %** of room. `g#15774`

**Gaps** (Mod, `g#17478, 16925, 16931, 15154`):
- **Big gap-up open**: put the buy order at the **lower wick** of the gap candle. That wick is also the stop if it breaks. Take a speculative target.
- A gap that **fills** is negative. A **close above the candle that made the gap** is positive.

**Zones, supports and patterns**
- **A long lower wick means the stock is at a support**; go find that support. `g#15753`
- **A support visited many times becomes fragile** and is easier to break. `g#17014`
- At a demand zone, **the entry pattern must complete**. If it doesn't, wait for a pattern at the next zone down. `g#16031–16037`
- **The strategy candle must be at a support**, like any pattern. `g#16916`
- **Failed inside bar → fakey**: if an inside bar completes, price breaks its stop, then **closes back above** the line, it becomes a fakey pattern. `g#15522`
- **Negative higher TFs override a lower-TF false break**: with bearish engulfing candles on the big TFs, the drop continued even after a false break completed. `g#16429, 16455`
- **RSI above 50 means more momentum.** `g#14866`
- Daily uptrend touching the **MA50**: drop to the 1 h chart and look for a setup there. `g#14665`

**Teacher**
- Use the pattern low as the stop. If it breaks, apply the false-stop-break techniques; if price keeps rising, use profit-trailing. **"The best TF for me is the 15 m."** You can also drop to a smaller TF to find a pattern with a clear stop. `g#17085–17086`
- One false-stop-break technique: **positive divergence** between the pattern low and the candle that broke it. `g#15235`

**Mod's routine**: analyze the whole market at night and set alerts; in the morning watch the **top gainers**. `g#15885, 16838`

### 8.7 The course period and after: Jul – Oct 2025
The group opened on 30 Jun 2025 with the course itself (lessons on 5–16 Jul 2025). In this period the teacher answered almost every question, so these are the most direct statements of the rules.

**Candle definitions confirmed** (teacher)
- **The four positive candles** `g#1264` (matches §1.1):
  1. **Buying candle**, change ≥ 3 % on the daily. Lines at its high and low. Positive **as long as price holds its low**.
  2. **Buying candle that opened with a gap down**: measure from its **open to its close**; ≥ 3 % counts. Its low line is the **previous close**. `g#997, 1000, 4346`
  3. **Bullish engulfing**: zone from its low to its **close** (not its high). No % or volume requirement. **Decided at its own close**; no confirming close needed («أحادية القرار»). `g#211, 853, 1093`
  4. **Volume candle**: lines at high and low. Positive on a **close above its high** without breaking its low. Its change % doesn't matter. `g#449`
- In short: buying candle → hold its low; engulfing → its close; volume candle → close above it. **"Close above a buying candle" is not an entry pattern.** `g#868, 2385, 4340`
- Selling-candle % = previous close → this close (`g#4764`). A hollow red candle whose open→close is ≥ 3 % still counts as buying. `g#454, 526`
- With a gap, buying/selling/volume candles are measured from the **previous close**. Pure shape patterns (inside bar, doji, spinning top, fakey) **ignore the gap**. `g#3260, 4232, 5241`
- Engulfing: the teacher accepts the **non-ideal** kind (body only), unless the engulfed candle has a very long upper wick. If an engulfing has high volume *and* a long upper wick, the cautious wait for a close above the wick. `g#380, 1597, 285`
- **Fakey** needs a mother candle, **at least one candle inside it**, then a break of the mother's low (wick or body), then a **close above the mother's high**. If the very next candle breaks the mother, it is not a fakey. Inside bar = mother not broken. `g#2263, 2429, 2454, 4086`
- On the 15 m chart a buying candle is **≥ 1 %**. `g#2446`

**Entry and stop** (teacher)
- Every pattern: draw the line at the high and **enter on a close above it**. The only exception is the engulfing, which is decided at its own close. `g#2296`
- **Stop = the lowest price between the pattern's line (e.g. the selling candle's high) and the candle that closed above it.** It must be **≤ 3 %**. It is set only after the pattern completes, and the trade has failed only on a **close below** it. `g#2137, 2367, 2482, 2697`
- No entry just because price reached a zone: **only on an intraday bullish pattern**. Zones come from the **1 h chart and higher**. `g#364, 1975, 1985`
- If the pattern is complete you can wait for a pullback test, or split the entry (especially if the stop is ≥ 2 %). Never enter with the whole portfolio. `g#1207, 3487, 5582`
- **Speculative target = 2–3× the stop.** After a close above a doji, the target is the gap top if it is ≥ 3 % away; if it is only ~1 %, split or wait for the close above the selling candle. `g#4353, 5666`
- Preferred entry TF is the **15 m**; drop to 5 m only when there is momentum at the start of the 15 m candle. Smaller TF = closer stop but more risk. `g#4769, 4257, 1919`

**Exits** (teacher): close below a shooting star; a bearish engulfing (exit at its close); a close below a volume candle; a close below a buying candle; a close below a doji after a rise. You can exit in two batches (shooting star, then buying candle). **"Never regret a profit."** Sell one tick before resistance. `g#1270–1273, 1607, 4033, 1206, 1573`

**Stop-break handling** (teacher, lesson 6): when a candle closes below the stop, mark that candle's low and trigger the stop only on a **close below it**. If there is **positive divergence**, the break is likely false; at worst exit at break-even when price comes back. Profit-trailing is done on a **TF smaller** than the entry TF, exiting on a bearish engulfing. `g#4036, 4039, 4037, 4608, 5401`

**News gaps** (teacher): gap-**up** on good news with high volume → line at the candle's body low, ignoring the gap; a close below it is an exit (the "good-news trap"). Gap-**down** on bad news with high volume → line at the body top; a close above is positive and the first target is the gap fill. `g#3221, 3327, 4767, 7486`

**Market and stock filters** (teacher)
- Market quality: traded value in the first hour **above about 1 bn SAR**, compared with the previous days. `g#3872, 4018`
- He avoids REITs, cement, banks, petrochemicals, large caps and non-sharia stocks; he trades speculative stocks. He holds nothing overnight before an earnings announcement. `g#3551, 4765, 7445`
- Don't open trades against tops, especially a top visited for the first time; check for negative divergence when tops are close together. `g#3686, 3980, 7690`
- Daily homework: for top gainers, find on the 15 m (two weeks) the pattern that started the move; for top losers, find the exit signal. `g#2121, 5609`

**Mod's strategies from this period**
- **Gap-up strategy** `g#6521, 7147, 7184, 7186`: draw a line at the **bottom of a gap-up candle**. When price comes back to it, **buy directly with no pattern**. Stop = a close below that candle (very close). Target 2–3 % the same day. Fast and risky; it rarely breaks on the first return.
- **Volume-MA candle strategy** (Sep 2025) `g#10389–10760, 10983, 10984; explained by members g#10561, 10746`: add a **20-period moving average on volume**. With the stock in a demand zone, take the **first green candle whose volume bar crosses above the volume MA**. Draw a line at its high and **enter on a close above it**. If price doesn't close above it and another such candle appears, move the line to the new one. The stop is the demand zone just below, so it is very close. The aim is to get in **before** the classic pattern (fakey, false break) completes.
- **Daily EMA screener** `g#13186`: EMA7 > EMA14 > EMA20 > EMA35 > EMA50, close > EMA7, RSI(14) ≥ 50, ROC(12) ≥ 0. He uses it only to find stocks; a single MA is fine too.
- Hollow candle on the daily `g#12484`: a close above the hollow candle into a volume candle's range → target the volume candle's top, stop under the hollow candle.
- In sharp declines **false breaks rarely work; "close above a volume candle" works best.** Stocks that broke tops on higher TFs give the most. `g#9322, 9340`
- Bad market: accept +1–1.5 %, small size; spread money over **at least 3 trades**. `g#9283, 12861, 12197`
- He gives a trade **3 trading days**: no stop hit and no target → exit. On small TFs he may place the stop on the 1 h or 30 m chart. `g#10822, 11496`
- After a bullish pattern, if a bearish engulfing follows, wait for a close above it. `g#8173`

> The group has now been read from its first message (30 Jun 2025) to 27 Nov 2026. Chart images are still not read.
