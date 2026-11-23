# Test Cases: Tarran T

**Team number:** [Use your team's number]
**My area:** Google Sync

---

**Test ID:** TT-01  
**From Part 6:** New  
**Written by:** Tarran Thomas  
**Title:** Exam information is converted into a Google Calendar event  
**Traces to:** REQ-TT-02  
**Test type:** Unit  
**Preconditions:** Python dependencies are installed. The project is available locally.  
**Test data:**
- Course: `CS 250`
- Title: `Final Exam`
- Date: `2026-12-01`
- Exam ID: `7`

**Steps:**
1. Open a Python terminal in the project directory.
2. Import `Exam` from `src.exam` and `GoogleCalendarService` from `src.google_calendar_service`.
3. Create an Exam object using the test data.
4. Call `GoogleCalendarService()._event_payload(exam)`.
5. Check the returned event information.

**Expected result:** The event has the summary `CS 250: Final Exam`, the start date `2026-12-01`, the end date `2026-12-02`, and the correct exam description.

**Actual result:** [The generated event payload contained the correct summary, description, start date, and end date.]  
**Status:** [Pass]  
**Severity:** [Only if Fail]  
**V or V:** [Only if Fail]  
**GitHub Issue:** [Only if Fail]

---

**Test ID:** TT-02  
**From Part 6:** New  
**Written by:** Tarran Thomas  
**Title:** Exam is saved when Google Calendar synchronization fails  
**Traces to:** REQ-TT-03  
**Test type:** Integration  
**Preconditions:** Flask is running. Google Calendar authorization is unavailable. Use a fresh test database.  
**Test data:**
- Course: `CS 250`
- Title: `Sync Failure Test`
- Date: `2026-12-02`

**Steps:**
1. Start the application without a valid Google Calendar authorization token.
2. Open the frontend and enter the test data.
3. Submit the exam.
4. Check the status message displayed by the application.
5. Check the saved exams using the `GET /events` endpoint.

**Expected result:** The exam is saved in the local database. The API returns HTTP 201 with `calendar_added` set to `false`. The frontend reports that the exam was saved locally but Google Calendar was not connected.

**Actual result:** [The API returned calendar_added: false but successfully saved the exam with the correct course, title, and date.] 
**Status:** [Pass]  
**Severity:** [Only if Fail]  
**V or V:** [Only if Fail]  
**GitHub Issue:** [Only if Fail]

---

**Test ID:** TT-03  
**From Part 6:** New  
**Written by:** Tarran Thomas  
**Title:** OAuth callback rejects a request without a valid state  
**Traces to:** REQ-TT-01  
**Test type:** Negative  
**Preconditions:** Flask is running. A fresh browser session is being used without an active OAuth authorization attempt.  
**Test data:**
- URL: `http://127.0.0.1:5000/oauth2callback`
- OAuth state: Missing

**Steps:**
1. Open a fresh private browser window.
2. Navigate directly to the OAuth callback URL.
3. Check the HTTP response and error message.

**Expected result:** The application returns HTTP 400 and displays an error indicating that the OAuth state is missing or expired. Authorization is not completed.

**Actual result:** [The OAuth callback returned an error stating that OAuth state was missing or expired.]  
**Status:** [Pass]  
**Severity:** [Only if Fail]  
**V or V:** [Only if Fail]  
**GitHub Issue:** [Only if Fail]

---

**Test ID:** TT-04  
**From Part 6:** New  
**Written by:** Tarran Thomas  
**Title:** Student successfully adds an exam to Google Calendar  
**Traces to:** G-TT-01, REQ-TT-01, REQ-TT-02  
**Test type:** Acceptance  
**Preconditions:** Flask is running. A valid Google OAuth credentials file is available. The student has access to a Google account for testing.  
**Test data:**
- Course: `CS 250`
- Title: `Google Sync Acceptance Test`
- Date: `2026-12-06`

**Steps:**
1. Open the application frontend.
2. Click Connect Google Calendar.
3. Sign in to a Google account and approve the requested permission.
4. Return to the application.
5. Enter the test exam information and submit it.
6. Open Google Calendar and locate the newly created event.

**Expected result:** The application reports that the exam was saved and added to Google Calendar. The event appears in the student's Google Calendar with the correct course, title, and date.

**Actual result:** [The API returned calendar_added: true, and the exam appeared correctly in Google Calendar on December 6, 2026, with the expected title and description.]  
**Status:** [Pass]  
**Severity:** [Only if Fail]  
**V or V:** [Only if Fail]  
**GitHub Issue:** [Only if Fail]

---

**Test ID:** TT-05  
**From Part 6:** New  
**Written by:** Tarran Thomas  
**Title:** Google OAuth requests only the required Calendar Events permission  
**Traces to:** NFR-TT-01  
**Test type:** Security  
**Preconditions:** Flask is running and a valid Google OAuth credentials file is available.  
**Test data:**
- Required permission: `https://www.googleapis.com/auth/calendar.events`

**Steps:**
1. Open the application frontend.
2. Click Connect Google Calendar.
3. Before approving authorization, inspect the Google authorization URL.
4. Find the `scope` parameter in the URL.
5. Check which permissions are requested.

**Expected result:** The authorization request asks only for the Google Calendar Events permission and does not request additional Google account permissions.

**Actual result:** [The source code declares only the Google Calendar Events scope and uses it throughout the OAuth authorization process. No additional scopes are explicitly requested.]  
**Status:** [Pass]  
**Severity:** [Only if Fail]  
**V or V:** [Only if Fail]  
**GitHub Issue:** [Only if Fail]
