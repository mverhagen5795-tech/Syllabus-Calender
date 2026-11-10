# Test Cases: Finja B.

**Team number:** 13
**My area:** user interface

<!--
HOW TO USE THIS FILE
1. Copy this file. Name the copy with your first name and last initial, like  maria-g.md
2. Leave TEMPLATE.md untouched for your teammates.
3. If a Part 6 test belongs to your area, upgrade it first and put it in the first block.
   Write at least 4 test cases using at least 3 test types. Include 1 Acceptance test that traces to your Stakeholder Goal.
   Run every test on the inherited system. Every Fail gets a GitHub Issue.
4. Copy the block between the lines for each new test case.
5. Test IDs: use your initials plus a number, like  MG-01, MG-02. This keeps IDs unique across your team.
   "Traces to" must name one of YOUR requirement IDs, like REQ-MG-02.
6. See docs/TESTING_FIELD_GUIDE.md for the sample test case TC-00.
-->

---

**Test ID:** FB-01
**From Part 6:** New
**Written by:** Finja Bruenen
**Title:** Exam page displays all exam-entry controls
**Traces to:** REQ-FB-01
**Test type:** System
**Preconditions:** The frontend is served and open in a browser.
**Test data:** None.

**Steps:**
1. Open the exam page.
2. Locate the Course and Title text inputs.
3. Locate the Date input and Add Event + button.

**Expected result:** The page displays one Course text input, one Title text input, one Date input, and one Add Event + button.
**Actual result:** The page displayed each of the four expected controls once.
**Status:** Pass
**Severity:** N/A
**V or V:** N/A
**GitHub Issue:** N/A

---

**Test ID:** FB-02
**From Part 6:** New
**Written by:** Finja Bruenen
**Title:** Student can enter an exam and see it in the exam list
**Traces to:** G-FB-01
**Test type:** Acceptance
**Preconditions:** The frontend and Flask backend are running. Google Calendar does not need to be connected.
**Test data:**
- Course: `CS 250`
- Title: `UI Test Exam`
- Date: `2026-12-10`

**Steps:**
1. Open the exam page.
2. Enter `CS 250` in Course, `UI Test Exam` in Title, and `2026-12-10` in Date.
3. Click Add Event +.

**Expected result:** The exam list displays `CS 250 - UI Test Exam - 2026-12-10`.
**Actual result:** The exam appeared in the list as `CS 250 - UI Test Exam - 2026-12-10`. The page reported that it was saved locally and Google Calendar was not connected.
**Status:** Pass
**Severity:** N/A
**V or V:** N/A
**GitHub Issue:** N/A

---

**Test ID:** FB-03
**From Part 6:** New
**Written by:** Finja Bruenen
**Title:** Saved exam appears in the list after reloading the page
**Traces to:** REQ-FB-02
**Test type:** Integration
**Preconditions:** The frontend and Flask backend are running, and the backend contains the test exam below.
**Test data:**
- Course: `CS 250`
- Title: `UI Test Exam`
- Date: `2026-12-10`

**Steps:**
1. Open or reload the exam page.
2. Wait for the initial `/events` request to finish.
3. Inspect the exam list.

**Expected result:** The exam list contains exactly one row for this test exam, displayed as `CS 250 - UI Test Exam - 2026-12-10`.
**Actual result:** After reloading, the exam list contained exactly one row: `CS 250 - UI Test Exam - 2026-12-10`.
**Status:** Pass
**Severity:** N/A
**V or V:** N/A
**GitHub Issue:** N/A

---

**Test ID:** FB-04
**From Part 6:** New
**Written by:** Finja Bruenen
**Title:** Page reports an error when saved exams cannot be loaded
**Traces to:** REQ-FB-03
**Test type:** Negative
**Preconditions:** The frontend is running, and the initial request to the Flask backend's `/events` endpoint is made to fail.
**Test data:** Simulate a network failure for `GET http://127.0.0.1:5000/events`.

**Steps:**
1. Make the initial `/events` request fail.
2. Open or reload the exam page.
3. Read the status message.

**Expected result:** The status message reads `Could not load saved exams from the Flask backend.`
**Actual result:** The status message read `Could not load saved exams from the Flask backend.`
**Status:** Pass
**Severity:** N/A
**V or V:** N/A
**GitHub Issue:** N/A

---
