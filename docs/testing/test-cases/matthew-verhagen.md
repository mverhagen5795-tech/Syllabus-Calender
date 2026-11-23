# Test Cases: [Your First Name Last Initial]

**Team number:** [13]
**My area:** [Main Feature]

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

**Test ID:** MV-01
**From Part 6:** TC-2
**Written by:** Matthew Verhagen
**Title:** AN exam with no course name is rejected
**Traces to:** REQ-MV-01
**Test type:** Negative
**Preconditions:** The aplication is running and the /events endpoint is available
**Test data:** POST /events with JSON "course": "", "title": "Midterm", "date": "2026-11-05"

**Steps:**
1.Start the Flask application with:
   ```powershell
   python app.py
2. Create test JSON using " 
$body = @{
    course = ""
    title = "Midterm"
    date = "2026-11-05"
} | ConvertTo-Json "
3.Send the request using "try {
    Invoke-RestMethod `
        -Uri "http://127.0.0.1:5000/events" `
        -Method POST `
        -ContentType "application/json" `
        -Body $body
}
catch {
    Write-Host "Status:" $_.Exception.Response.StatusCode.value__
    Write-Host "Response:" $_.ErrorDetails.Message
}"

**Expected result:**The server returns HTTP 400 and error message "course, title, and date are required"
**Actual result:**The server returns HTTP 400 and error message "course, title, and date are required"
**Status:** Pass
**Severity:** N/A
**V or V:** N/A
**GitHub Issue:** N/A

---

**Test ID:** MV-02
**From Part 6:** TC-3
**Written by:** Matthew Verhagen
**Title:** The Shortest valid course name is accepted
**Traces to:** REQ-MV-02
**Test type:** Boundary
**Preconditions:** The application is running and /events is working
**Test data:** POST / events with JSON "course": "A", "title": "Midterm", "date": "2026-11-05"

**Steps:**
1.Start the Flask application by running:
   ```powershell
   python app.py
2.Create test JSON using "$body = @{
    course = "A"
    title = "Midterm"
    date = "2026-11-05"
} | ConvertTo-Json"
3.Send test request " try {
    $response = Invoke-RestMethod `
        -Uri "http://127.0.0.1:5000/events" `
        -Method POST `
        -ContentType "application/json" `
        -Body $body

    Write-Host "Status: 201"
    $response | ConvertTo-Json
}
catch {
    Write-Host "Status:" $_.Exception.Response.StatusCode.value__
    Write-Host "Response:" $_.ErrorDetails.Message
}"

**Expected result:** Server returns 201 and the JSON reponse contains Course "A", title "Midterm" and date " 2026-11-05"
**Actual result:**Server returns 201 and the JSON reponse contains Course "A", title "Midterm" and date " 2026-11-05"
**Status:** Pass
**Severity:**N/A
**V or V:** N/A
**GitHub Issue:** N/A

---

**Test ID:** MV-03
**From Part 6:** New
**Written by:** Matthew Verhagen
**Title:** A sumbited exam is aved and visible in events list
**Traces to:** G-MV-01
**Test type:** Acceptance
**Preconditions:** The application is running with an available local database
**Test data:**

**Steps:**
1.Start the Flask application by running:
   ```powershell
   python app.py
2. Create test json "$body = @{
    course = "CS 250"
    title = "Final Exam"
    date = "2026-12-10"
} | ConvertTo-Json"
3. Sumbit exam to /events with "$postResponse = Invoke-RestMethod `
    -Uri "http://127.0.0.1:5000/events" `
    -Method POST `
    -ContentType "application/json" `
    -Body $body

$postResponse | ConvertTo-Json"
4. Request the saved events with "$events = Invoke-RestMethod `
    -Uri "http://127.0.0.1:5000/events" `
    -Method GET

$events | ConvertTo-Json"

**Expected result:** The POST request returns HTTP status 201, and the GET response contains the saved exam with course "CS 250", title "Final Exam", and date "2026-12-10"
**Actual result:**he POST request returns HTTP status 201, and the GET response contains the saved exam with course "CS 250", title "Final Exam", and date "2026-12-10"
**Status:** Pass
**Severity:** N/A
**V or V:** N/A
**GitHub Issue:** N/A

---

**Test ID:** MV-04
**From Part 6:** New
**Written by:** Matthew Verhagen
**Title:** A request missing a required field is rejected without saving the event
**Traces to:** REQ-MV-01
**Test type:** Integration
**Preconditions:** The application is running with an avaiable local database
**Test data:** POST /events` with JSON body  "course": "CS 250", "title": "", "date": "2026-12-10" 

**Steps:**
1.Start the Flask application by running:
   ```powershell
   python app.py
2.Create invalid test data using "$body = @{
    course = "CS 250"
    title = ""
    date = "2026-12-10"
} | ConvertTo-Json"
3.Send the invalid exam request with "try {
    Invoke-RestMethod `
        -Uri "http://127.0.0.1:5000/events" `
        -Method POST `
        -ContentType "application/json" `
        -Body $body
}
catch {
    Write-Host "Status:" $_.Exception.Response.StatusCode.value__
    Write-Host "Response:" $_.ErrorDetails.Message
}"
4. Request the saved events using "$events = Invoke-RestMethod `
    -Uri "http://127.0.0.1:5000/events" `
    -Method GET

$events | ConvertTo-Json"

**Expected result:**The POST request returns HTTP status 400 with the error message "course, title, and date are required". The invalid exam is not saved in the events list
**Actual result:**The POST request returns HTTP status 400 with the error message "course, title, and date are required". The invalid exam is not saved in the events list
**Status:** Pass
**Severity:**N/A
**V or V:**N/A
**GitHub Issue:**N/A

---
