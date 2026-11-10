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
