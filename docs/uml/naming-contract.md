# Naming Contract

Classes used by more than one slice. Only the owner writes the code stub for that class. Everyone else uses it with these exact names.

| Class           | Owner   | Used By                      |
|-----------------|---------|------------------------------|
| Exam            | Rory    | Rory, Ubay, Deandre, Gabe    |
| Student         | Gabe    | Rory, Ubay, Deandre, Gabe    |
| GoogleCalendarService | Deandre | Rory, Deandre                |

## Exam attributes
- exam_id: int
- course: str
- title: str
- date: date

## Student attributes
- student_id: int
- email: str

## GoogleCalendarService attributes
- calendar_id: str

## Rules
- If you need a shared class that is not on this list, add it here and tell the team the same day.
