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

### 1.3 Other candle shapes used (course B, `msg 94`; course A, `msg 43`)
- **Inside bar / harami** الأنسايد بار (الهرامي، المرأة الحامل): a mother candle with one or more candles fully inside it. *Fewer inside candles = stronger.* (`msg 43 @15:35`)
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

### 2.1a The 7 zones as spoken in lesson 1 — `[audio]` (confirmed from the transcript)

| # | Zone | What the presenter adds out loud |
|---|---|---|
| 1 | **Uptrend** (المسار الصاعد): higher highs and higher lows | Called "the backbone" of high-probability trades. **But be careful** if price in an uptrend faces a previous resistance, a big moving average, or a supply zone. Example: buying at 86 "because the trend is up", then price fell back to 57. |
| 2 | **Previous low** that price rose from, then came back to | Mark the bottom candle's **high and low**. On the return, drop to a smaller timeframe and look for a pattern that shows the buyer is defending the zone. Example: rose 66 to 86, then came back. |
| 3 | **Volume candle** | Has **two** zones: (a) **a close above the volume candle** (positivity in the *current* zone), and (b) **a return to it after price rose from it** (the *opposite* zone). Volume bar = higher than the previous bars. **Preferably after a decline.** If there's a gap, measure from the previous close. A close above it shows the buyer is winning, and it's stronger after an uptrend or a sideways range. "Only market makers can print volume candles. **Volume is the key to truth**" (الفوليوم مفتاح الحقيقة). Example used the weekly as the higher TF and 1 h as the lower one. |
| 4 | **Prominent buying candle** that price rose from, then came back to | Only a strong buyer can print it (example: one week from 71 to 90). **The zone runs from its low to its close, not its high**, because change % is measured on closes. On a return to it, look for a bullish pattern. |
| 5 | **Broken previous high** | A top is a seller's zone. Once price **closes above it** and rises, it becomes a buyer's zone. Mark the top's high and low. On a retest, look for a bullish pattern on the lower TF. "Only a strong buyer can break a previous high and rise after it", so expect him to defend it. Example: +48 % after the retests. |
| 6 | **Broken long selling candle**: a "price trap" (مصيدة سعرية), which he calls «انتفاء السلبية» | Logic says price should keep falling after a strong selling candle. If it **closes above the selling candle's high** instead, the negativity is cancelled and becomes a trap in favour of buyers. **The close above it is enough** to make the zone valid. A later return to it is also a buy zone. Example: a selling candle of −16 % that price closed above. Same logic as a close above a volume candle. |
| 7 | **Fibonacci 50 % / 61.8 %** | Draw the Fib on the wave with **0 at the top and 100 at the bottom**. Wait for price at the **50 %** or **61.8 %** level, "the most worthy levels". Then drop to a smaller TF for a bullish pattern. |

Each zone is only a *permission* to buy; **the entry always needs a bullish pattern on the lower timeframe** inside it.

### 2.2 Where sellers (supply) sit — لصالح البيع (`msg 26`, lesson 2)
Mirror of 2.1: downtrend (lower highs and lower lows) `@2:45`; previous tops `@4:45`; volume candles, selling candles and long buying candles that price fell from and has returned to; a **broken bottom** when price comes back up to it `@15:00`.

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

### 3.2 Course B versions of the same ideas
- **High-volume candle model** شمعة الكميات العالية (`msg 107`): *"the positive model is to break it first, then return and close above it, in an uptrend"*. In other words: price dips below the high-volume candle, then closes back above it.
- **Buying-candle break model** نموذج كسر الشمعة الشرائية (`msg 110`): buying candle → broken → close back above = positive. **Stop: under the lowest point between the broken candle and the closing candle.**
- **Selling-candle model** الشمعة البيعية (`msg 112`): a selling candle in an uptrend, then **a close above it** → buy. **Stop: below the selling candle's low.**
- **False break** = "a break of a bottom" (`msg 103`).
- **Divergence** (`msg 114`): positive at bottoms, negative at tops, RSI.

### 3.3 Sell-side patterns (`msg 26` part 2: النماذج اللحظية الداعمة للهبوط)
False breakout above the zone high, negative divergence, **shooting star** الشهاب, bearish engulfing, doji, break of a buying candle, break of a volume candle. Example: a 15 m false breakout inside a zone made by a broken volume candle that price came back up to. (`msg 26 @19:00–25:00`)

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
- **Target:** the slides don't give a fixed rule. The examples measure +3 % to +8 % moves to the next opposing zone (supply / previous top), e.g. `msg 43 @7:20` +7.6 %, `@15:35` +4.9 %, `@30:50` +5.7 %. *Exact exit rule: to be confirmed in the audio pass.*
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
TARGET: next HTF supply zone / previous top (no fixed % in slides)
```

---

## 7. Gaps — what's still missing

- **Spoken content**: lesson 1 (`msg 7`) is done `[audio]`. Still missing: lessons 2–5 (`msg 26, 43, 67, 73`), the discussion videos (`msg 8, 27, 44, 68, 74`; lesson 1 says the discussion «لا تقل أهمية» than the lesson), the live session (`msg 76`), and course B's long lessons. The user is supplying transcripts.
- Exact volume-candle threshold, exit/target rule, and position sizing: not on any slide.
- PDFs: download-protected.
- Lesson 5 (`msg 73`, screen design) is a TickerChart setup walkthrough: no trading rules on screen.

---

## 8. Practice group: answers from "Mod" and the teacher — `[group]`

Source: the discussion group **«احتراف المضاربات اللحظية ٩»**, where students apply what the channel teaches.
Two accounts matter: **"Mod ."** (Abu Khalid, `@modee_14`, the most active member: about 1,300 of 3,900 messages read so far)
and **the teacher himself, "أحمد ( أبو عبدالله )"** (`@Ahmed_Abuabullah`). References are group message numbers (`g#N`).
Coverage so far: **7 Jan – 27 Nov 2026** (messages `g#17490–26794`). Older history is still being read.
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

> Not yet read: the group's history before 7 Jan 2026, and the chart images themselves.
