Test Cases: [Poulina R]
Team number: [13] My area: [Data Storage]

Test ID: From Part 6: TC-PR-02 Written by: Poulina Reipolska Title: Exam with an empty course name is rejected and not stored Traces to: REQ-PR-03 Test type: Negative Preconditions: Flask server running Test data: Course: (empty), Title: Midterm, Date: 10/31/2025 

Steps: 
1. Open frontend/index.html.
2. Leave Course empty, type Midterm, pick 10/31/2025.
3. Click Add Event +.
4. Open http://127.0.0.1:5000/events.

Expected result: The server responds with HTTP 400 and GET /events still returns []
Actual result: Flask log shows POST /events returned 400. GET /events returned [], so no row was stored.
Status: Pass Severity: N/a V or V: N/a GitHub Issue: N/a

Test ID: From Part 6: (old test number, or New) Written by: Title: Traces to: Test type: Preconditions: Test data:

Steps: 1. 2. 3.

Expected result: Actual result: Status: Severity: V or V: GitHub Issue:

Test ID: From Part 6: (old test number, or New) Written by: Title: Traces to: Test type: Preconditions: Test data:

Steps: 1. 2. 3.

Expected result: Actual result: Status: Severity: V or V: GitHub Issue:

Test ID: From Part 6: (old test number, or New) Written by: Title: Traces to: Test type: Preconditions: Test data:

Steps: 1. 2. 3.

Expected result: Actual result: Status: Severity: V or V: GitHub Issue:

