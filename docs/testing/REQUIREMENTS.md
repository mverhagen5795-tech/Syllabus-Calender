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
