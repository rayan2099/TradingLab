# Candles & Volume Rules — الشموع والكميات

Extracted from the Telegram channel **«الـمـلـخـص ٩»** only (the user's study channel), Nov 2026.
Source references use the channel's message number (`msg N`) and, for videos, the time in the video (`@mm:ss`).

> **Status: slides + text only (draft 1).** The lessons are slide decks and every slide was read frame by frame.
> What the presenter says *only out loud* is **not yet included**. An audio pass (Arabic dictation while the
> lessons play) is in progress; rules it adds or changes will be marked `[audio]`.
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
1. **General uptrend** (higher highs and higher lows). `@9:48`
2. **Previous bottoms** that price rose from and has now returned to. `@11:32`
3. **Volume candles** that price rose from and has returned to: only market makers can print them. `@12:47`
4. **Prominent buying candles** that price rose from and has returned to. `@14:47`
5. **A broken (breached) top**: after the breakout, price comes back to it (retest). `@16:32`
6. **A long selling candle that was breached**: price rose above it, then came back to it. `@18:17`
7. **A close above a volume candle**: buyer superiority, even after a downtrend or a range. `@21:05`
8. **A close above a selling candle.** `@21:47`
9. **Fibonacci retracements 50 % and 61.8 %** of the prior up-move. `@22:32`

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
  - prior bottom / broken prior top / breached long selling candle / HTF volume candle price rose from
  - 50%-61.8% retracement of the last up-leg
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
TARGET: next HTF supply zone / previous top (no fixed % in slides)
```

---

## 7. Gaps — what's still missing

- **Spoken content** of all lessons and the discussion videos (`msg 8, 27, 44, 68, 74`), the live session (`msg 76`), and course B's long lessons. In progress.
- Exact volume-candle threshold, exit/target rule, and position sizing: not on any slide.
- PDFs: download-protected.
- Lesson 5 (`msg 73`, screen design) is a TickerChart setup walkthrough: no trading rules on screen.
