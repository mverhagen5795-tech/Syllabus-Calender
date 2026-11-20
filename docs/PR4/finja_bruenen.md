# Finja Bruenen

## Bug 1: CreateExamTimer constructor syntax

- **Issue:** Not filed; kept local as requested.
- **PR:** Not created as requested.
- **Before:** ![CreateExamTimer before fix](./screenshots/finja_bruenen_issue1_before.png)
- **After:** ![CreateExamTimer after fix](./screenshots/finja_bruenen_issue1_after.png)
- **Classification:** Code bug. The original `def__init__` declaration caused a `SyntaxError`; the corrected constructor imports and its focused test passes.

## Bug 2: DisplayExamTimes constructor syntax

- **Issue:** Not filed; kept local as requested.
- **PR:** Not created as requested.
- **Before:** ![DisplayExamTimes before fix](./screenshots/finja_bruenen_issue2_before.png)
- **After:** ![DisplayExamTimes after fix](./screenshots/finja_bruenen_issue2_after.png)
- **Classification:** Code bug. The original `def__init__` declaration caused a `SyntaxError`; the corrected constructor imports and its focused test passes.

**Evidence note:** The PNGs are terminal-style renderings of the actual before/after command output, not raw desktop captures.

**AI disclosure:** Copilot assisted in identifying and fixing both syntax errors and in adding focused regression tests.
