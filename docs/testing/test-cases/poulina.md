Test Cases: Poulina R
Team number: 13 My area: Data Storage

Test ID: From Part 6: TC-PR-02 Written by: Poulina Reipolska Title: Exam with an empty course name is rejected and not stored Traces to: REQ-PR-03 Test type: Negative Preconditions: Flask server running Test data: Course: (empty), Title: Midterm, Date: 10/31/2025 

Steps: 
1. Open frontend/index.html.
2. Leave Course empty, type Midterm, pick 10/31/2025.
3. Click Add Event +.
4. Open http://127.0.0.1:5000/events.

Expected result: The server responds with HTTP 400 and GET /events still returns []
Actual result: Flask log shows POST /events returned 400. GET /events returned [], so no row was stored.
Status: Pass Severity: N/a V or V: N/a GitHub Issue: N/a

Test ID: TC-PR-01 From Part 6: (old test number, or New) Written by: Poulina Reipolska Title: Poulina Reipolska Traces to: REQ-PR-01 Test type: Integration Preconditions:Flask server running Test data:cs 250, Title: Midterm, Date: 11/05/2026

Steps: 
1. Open frontend/index.html.
2. Enter the test data in the form and click Add Event +.
3. Note the status code on the POST /events line in the Flask terminal.
4. Open http://127.0.0.1:5000/events.

Expected result: POST/events returns 201 or 200 and GET/events returns one exam Actual result: GET /events returned one exam: course cs 250, title Midterm, date 2025-10-31, matching the input. Post /events returned 201 Status: Pass Severity: N/a V or V: N/a GitHub Issue: N/a

Test ID: TC-PR-03 From Part 6: (old test number, or New) Written by: Title: SQL text in a course name is stored as plain text Traces to: NFR-PR-02 Test type: Security Preconditions: Flask server running + events.db exists and contains the cs 250 exam from TC-PR-01  Test data: Course: x'); DROP TABLE events;--, Title: Midterm, Date: 11/06/2025 (stored as 2025-11-06)

Steps: 
1. Open frontend/index.html.
2. Enter the test data and click Add Event +.
3. Note the status code on the POST /events line in the Flask terminal.
4. Open http://127.0.0.1:5000/events.

Expected result: POST /events returns 200 or 201. GET /events still works and lists both exams, including one whose course is exactly x'); DROP TABLE events;--. Actual result: GET /events returned both exams. The second has course exactly x'); DROP TABLE events;--, title Midterm, date 2025-11-06. The events table still exists and the first exam is intact. "POST /events HTTP/1.1" 201  Status: Pass Severity: N/a V or V: GitHub Issue:

Test ID: From Part 6: (old test number, or New) Written by: Title: Traces to: Test type: Preconditions: Test data:

Steps: 1. 2. 3.

Expected result: Actual result: Status: Severity: V or V: GitHub Issue:

