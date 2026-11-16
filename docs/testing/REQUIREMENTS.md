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

## Section: [Your Area] ([Your Name])

### Stakeholder Goals

| ID | Stakeholder | Goal |
|---|---|---|
| G-XX-01 | | |

### Functional Requirements

| ID | Requirement | Status | From Part 5 |
|---|---|---|---|
| REQ-XX-01 | | | |
| REQ-XX-02 | | | |
| REQ-XX-03 | | | |

### Non-Functional Requirements

| ID | Requirement | Status | From Part 5 |
|---|---|---|---|
| NFR-XX-01 | | | |

### Example of a Good Rewrite

| ID | Requirement | Status | From Part 5 |
|---|---|---|---|
| REQ-MG-01 | The system shall reject a profile bio longer than 280 characters with the error "Bio must be 280 characters or fewer." | Suspected bug | CR-3 (Unconfirmed): The system shall limit the bio to 280 characters. |
| NFR-MG-01 | The profile page loads in under 2 seconds with 100 profiles in the database. | Confirmed | New |

---

## Section: [Your Area] ([Your Name])

### Stakeholder Goals

| ID | Stakeholder | Goal |
|---|---|---|
| | | |

### Functional Requirements

| ID | Requirement | Status | From Part 5 |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

### Non-Functional Requirements

| ID | Requirement | Status | From Part 5 |
|---|---|---|---|
| | | | |

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
