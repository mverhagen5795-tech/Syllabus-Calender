# Traceability Matrix

**Team number:** 13
**Filled in by (captain):** [Matthew Verhagen]

## Requirements to Tests

| Requirement ID | From Part 5 | Owner             | Test case IDs       | Result  | GitHub Issue # |
| -------------- | ----------- | ----------------- | ------------------- | ------- | -------------- |
| REQ-FB-01      | New         | Finja Bruenen     | FB-01               | Pass    | N/A            |
| REQ-FB-02      | New         | Finja Bruenen     | FB-03               | Pass    | N/A            |
| REQ-FB-03      | New         | Finja Bruenen     | FB-04               | Pass    | N/A            |
| NFR-FB-01      | CR-5        | Finja Bruenen     | None                | No test | N/A            |
| REQ-PR-01      | CR-1        | Poulina Reipolska | TC-PR-01            | Pass    | N/A            |
| REQ-PR-02      | New         | Poulina Reipolska | TC-PR-04            | Pass    | N/A            |
| REQ-PR-03      | CR-3        | Poulina Reipolska | TC-PR-02            | Pass    | N/A            |
| NFR-PR-01      | New         | Poulina Reipolska | TC-PR-03            | Pass    | N/A            |
| TT-01          | CR-2        | Tarran Thomas     | TT-04               | Pass    | N/A            |
| TT-02          | CR-4        | Tarran Thomas     | TT-02               | Pass    | N/A            |
| TT-03          | CR-4        | Tarran Thomas     | TT-02               | Pass    | N/A            |
| NFR-TT-01      | New         | Tarran Thomas     | TT-05               | Pass    | N/A            |
| REQ-MV-01      | CR-3        | Matthew Verhagen  | MV-01, MV-04        | 2 Pass  | N/A            |
| REQ-MV-02      | New         | Matthew Verhagen  | MV-02               | Pass    | N/A            |
| REQ-MV-03      | New         | Matthew Verhagen  | MV-03               | Pass    | N/A            |
| NFR-MV-01      | New         | Matthew Verhagen  | MV-01, MV-02, MV-04 | Pass    | N/A            |

## Gaps

- `NFR-FB-01` has no test case.

- Part 6 `TC-2` appears in both Poulina's and Matthew's test files. 

## Test Type Coverage

| Test type      | Test ID                       |
| -------------- | ----------------------------- |
| Unit           | TT-01                         |
| Integration    | TC-PR-01, TT-02, FB-03, MV-04 |
| System (E2E)   | FB-01                         |
| Acceptance     | TC-PR-04, FB-02, TT-04, MV-03 |
| Boundary Value | MV-02                         |
| Negative       | TC-PR-02, FB-04, TT-03, MV-01 |
| Security       | TC-PR-03, TT-05               |

## Validation Findings

| Requirement ID | Goal it fails | Why                                                                                                                                                                                                                                  | Issue # |
| -------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| None           | N/A           | No validation finding was recorded. The requirements describe saving exams, displaying them, preserving them, handling invalid input, and synchronizing with Google Calendar, which all directly support our stated goals. | N/A     |

## Summary

|                                  | Count              |
| -------------------------------- | ------------------ |
| Part 5 requirements carried over | 6 requirement rows |
| New requirements added           | 10                 |
| Part 6 tests upgraded (out of 3) | 3                  |
| Total requirements               | 16                 |
| Total test cases                 | 16                 |
| Passed                           | 16                 |
| Failed                           | 0                  |
| Issues opened                    | 0                  |
| Critical issues                  | 0                  |

**In one sentence, would you ship this system today? Why or why not?**
No not yet even though all our tests passed we still have to work on some of the UI and tests that come with that.
