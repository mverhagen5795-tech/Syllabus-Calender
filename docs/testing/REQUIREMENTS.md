# Testable Requirements: [Project Name]

**Team number:** [XX]
**Inherited from:** Team [XX]

## Who Owns What

| Area of the system | Owner | ID prefix |
|---|---|---|
| user interface | Finja Bruenen | FB |
| data storage | Poulina Reipolska | PR |
| google sync | Tarran Thomas | TT |
| main feature | Matthew Verhagen | MV |

<!-- 
user interface: CR-5
google sync: CR-2, CR-4
main feature: CR-3, TC-2, TC-3 
data storage: CR-1, TC-1
 -->



<!--
RULES
- Only edit YOUR OWN section below. This keeps merge conflicts away.
- Categories: G = Stakeholder Goal, REQ = Functional, NFR = Non-Functional.
- "From Part 5": write the original CR ID and its text from SYSTEM_MAP.md. Write "New" if you added it this sprint.
- Status: Confirmed or Suspected bug. No Unconfirmed allowed. Every Suspected bug needs a GitHub Issue.
- The test: could a stranger write a Pass or Fail test without asking you a question?
-->

---

## Section: user interface (Finja Bruenen)

### Stakeholder Goals

| ID | Stakeholder | Goal |
|---|---|---|
| G-FB-01 | Student | Enter exam details and view the exam list. |


### Functional Requirements

| ID | Requirement | Status | From Part 5 |
|---|---|---|---|
| REQ-FB-01 | The system shall provide Course and Title text inputs, a Date input, and an Add Event button on the exam page. | Confirmed | New |
| REQ-FB-02 | The system shall display each exam returned by the initial `/events` request in the exam list as `course - title - date`. | Confirmed | New |
| REQ-FB-03 | The system shall display the message "Could not load saved exams from the Flask backend." when the initial `/events` request fails. | Confirmed | New |

### Non-Functional Requirements

| ID | Requirement | Status | From Part 5 |
|---|---|---|---|
| NFR-FB-01 | The system shall use the configured backend base URL for both exam-loading and exam-submission requests to the `/events` endpoint. | Suspected bug | CR-5 (Unconfirmed): System shall send requests to a configurable ip address |

### Example of a Good Rewrite

| ID | Requirement | Status | From Part 5 |
|---|---|---|---|
| REQ-MG-01 | The system shall reject a profile bio longer than 280 characters with the error "Bio must be 280 characters or fewer." | Suspected bug | CR-3 (Unconfirmed): The system shall limit the bio to 280 characters. |
| NFR-MG-01 | The profile page loads in under 2 seconds with 100 profiles in the database. | Confirmed | New |

---

## Section: [Data Storage] ([Poulina Reipolska])

### Stakeholder Goals

| ID | Stakeholder | Goal |
|---|---|---|
|G-PR-01|Student|Exames that are added will stay even if the servers are reset, no making students filling out tables multiple times|

### Functional Requirements

| ID | Requirement | Status | From Part 5 |
|---|---|---|---|
|REQ-PR-01|When a valid exam (course, title, date) is submitted, exactly one matching row is saved and GET /events returns it with the same course, title, and date.|Confirmed|CR-1|
|REQ-PR-02|After the Flask server is stopped and restarted from the same folder, every exam saved before the restart is still returned by GET /events.|Confirmed |New|
|REQ-PR-03|When an exam with an empty course name is submitted, the system returns HTTP 400 and no row is added to the events table.|Confirmed|CR-3|

### Non-Functional Requirements

| ID | Requirement | Status | From Part 5 |
|---|---|---|---|
|NFR-PR-01|A course name containing SQL text (such as x'); DROP TABLE events;--) is stored as plain text, and the events table still exists afterward.|Confirmed|New|

---

## Section: [Google Sync] ([Tarran Thomas])

### Stakeholder Goals

| ID | Stakeholder | Goal |
|---|---|---|
|G-TT-01|Student|Students want their saved exams to appear in Google Calendar so they can keep track of upcoming exams without entering them manually.|

### Functional Requirements

| ID | Requirement | Status | From Part 5 |
|---|---|---|---|
|TT-01|When a user has authorized Google Calendar access, the system shall create a Google Calendar event for each submitted exam.|Confirmed*|CR-2: System shall create a Google Calendar event for each exam.|
|TT-02|If Google Calendar authorization is unavailable or event creation fails, the system shall still save the submitted exam in the local database.|Confirmed*|CR-4: System shall keep an exam while reporting a Google Calendar sync error.|
|TT-03|If Google Calendar synchronization fails, the system shall return HTTP status 201 and include "calendar_added": false in the response.|Confirmed*|CR-4: System shall keep an exam while reporting a Google Calendar sync error.|

### Non-Functional Requirements

| ID | Requirement | Status | From Part 5 |
|---|---|---|---|
|NFR-TT-01|The system shall request only the Google Calendar Events permission (calendar.events) when asking users to authorize Google Calendar access.|Confirmed*|New|


---

## Section: Main Feature (Matthew Verhagen)

### Stakeholder Goals

| ID | Stakeholder | Goal |
|---|---|---|
|G-MV-01|Student |Students are required to sumbit an exam with its course, title, and date and then get confirmation that that information was saved to their calander |

### Functional Requirements

| ID | Requirement | Status | From Part 5 |
|---|---|---|---|
|REQ-MV-01 |When a client sends POST /events with an empty, course, title, or date, the system shall return HTTP status 400 and the JSON error course,title, and date required |Confirmed |Cr-3: System shall reject an exam with no course name |
|REQ-MV-02 |When a client sends POST /events with course,title, and date fields that arent empty, the system shall save the exam and return HTTP status 201 with the submitted exam fields in the JSON |Confirmed |New |
|REQ-MV-03 |When a cleint request GET /events, the system shall return HTTP status 200 and a JSON array containing the exams saved locally |Confirmed |New |

### Non-Functional Requirements

| ID | Requirement | Status | From Part 5 |
|---|---|---|---|
|NFR-MV-01 |the /events API shall use JSON for request and response data, inclduing JSON error responses for invalid requests|Confirmed |New |
