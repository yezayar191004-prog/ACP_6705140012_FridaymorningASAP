# Assignment 03 — CHANGES

**Name:** ______________________  **Student ID:** ______________________

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | Product data was stored as bare tuples and indexed by position. | Replaced with a `Product` class holding `name`, `price`, and `category`, and `OrderItem` objects for quantities. | Classes / composition | Ran `python3 Assignment_03.py` and checked the exact receipt output matched the golden output. |
| 2 | Customer tiers were implemented with repeated `if t == ...` logic for both discount and points. | Introduced a `Customer` base class with `NoneCustomer`, `SilverCustomer`, `GoldCustomer`, and `PlatinumCustomer` subclasses. | Polymorphism | Verified the output remained identical and that no tier chain remained in the calculation methods. |
| 3 | Totals and taxes were mixed into one large function and printed directly while also calculating. | Moved calculations into pure methods such as `subtotal()`, `discount()`, `tax()`, `total()`, and `points()`. | Pure functions / separation of concerns | Compared the generated receipt text and totals against the legacy output and ran the self-test until it passed. |
| 4 | State was not validated and the code relied on magic numbers like `0.07`, `10`, and `100`. | Added constructor validation and named constants such as `TAX_RATE`, `DISCOUNT_THRESHOLD`, and `BULK_QTY_THRESHOLD`. | Encapsulation | Executed the script and confirmed the same values were produced without changing the output format. |
| 5 | The legacy output was hard to maintain because the receipt text and calculations were interleaved. | Added `Order.receipt()` to build the printable receipt and kept calculation logic separate from printing. | Interface vs implementation | Ran the self-test and checked the output string for each order and the grand total exactly matched. |

## 2 · Short reflection (4–6 sentences)

The biggest improvement was moving the business rules into object methods instead of leaving them in one giant function. That made the code easier to understand because each class owns one responsibility: products know their price/category, items know their quantity, orders know how to calculate totals, and customers know their discount and points behavior. Keeping the behaviour identical was the hardest part because even small differences in rounding or blank lines would fail the self-test, so I matched the legacy formatting carefully. I also kept the same rules for tax, tier discounts, bulk discounts, and points calculation exactly as they were in the original program. This refactor was about preserving behaviour while improving structure, not changing the business logic in any way.

---

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | "Refactor this messy store logic into clean OOP classes while keeping the same output." | Suggested a `Product` + `OrderItem` + `Customer` + `Order` design and a polymorphic customer tier family. | Edited | Ran the script with `python3 Assignment_03.py` and matched the exact golden output. |
| 2 | "How do I keep the receipt text identical while separating calculation from printing?" | Recommended pure methods for subtotal/discount/tax/total/points, with `receipt()` building only the textual output. | Accepted | Self-test passed and the line-by-line receipt matched the legacy output. |
| 3 | "How do I structure the customer discount and points logic without using if tier==... checks?" | Recommended a `Customer` superclass and subclass discount-rate overrides plus a factory to map strings to objects. | Edited | Reviewed the final code and confirmed the script still printed PASS. |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

---

## 4 · Before-you-submit checklist

- [x] `python Assignment_03.py` prints **PASS**.
- [x] No tuples / parallel lists left — products, orders, and items are objects.
- [x] No `if tier == ...` chains — tiers are a class family.
- [x] Calculation methods **return** values and do not `print`; printing is separate.
- [x] Constructors validate state; no leftover `global`; magic numbers are named.
- [x] The change table and reflection above are filled in.
- [x] The prompt log is complete and the ownership statement is signed.
