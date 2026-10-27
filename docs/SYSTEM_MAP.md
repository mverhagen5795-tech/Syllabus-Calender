# **Trace the Click: System Map**

Oct 22, 2026 · @Manju Muralidharan

## **Instructions**

You are not fixing anything today. You are reading. Your team will map the inherited system as it actually exists, not as the handoff docs say it exists.

* **Time:** 40 minutes.  
* **Goal:** Trace one user action end to end and draw the as-built architecture.  
* **Submit:** Commit this map to your repo as docs/SYSTEM\_MAP.md with the diagram as an image and submit a photo of the paper version.  
* **Rule:** Every claim needs proof in the code. "Probably somewhere in utils" does not count.  
* **AI use:** AI may explain unfamiliar syntax. The diagram and trace must come from your own reading of the code.

| Time | Phase |
| :---- | :---- |
| 0 to 5 min | Pick one user action that touches the backend and database |
| 5 to 15 min | Draw the architecture diagram |
| 15 to 30 min | Tracers trace their halves. Analyst and Architect start Part 4\. |
| 30 to 35 min | Cross-check: each person explains one section they did not write to a teammate. |
| 35 to 40 min | Clean up and submit |

## **Team and roles**

**Team name:**

**Inherited project:**

Each of the four members owns one part of the map. Everyone reads code. Nobody spectates.

| Role | Owns | Specific task | Name |
| :---- | :---- | :---- | :---- |
| Product Analyst | Part 1 and the questions in Part 4 | Runs the app, picks the user action, writes the purpose sentence, and collects the team’s three questions for the original team. | Tarran Thomas |
| Architect | Part 2 and the mismatches in Part 4 | Draws the as-built diagram from the code, then compares it to the handoff UML and records every mismatch. | Finja Bruenen |
| Frontend Tracer | Part 3, client side | Traces the action from the button click to the request leaving the client. Every row gets a file path. | Poulina Reipolska |
| Backend Tracer | Part 3, server side | Traces from the API route to the database and back to the response. Every row gets a file path. | Matthew Verhagen |
|  | Part 5 and 6 | Adding candidate requirements  and unit test cases | Poulina Reipolska, Finja Bruenen |

The two Tracers must meet at the same API endpoint. If your halves don’t connect, your trace is wrong.

## **Part 1: Purpose**

In one sentence: what does this system do, and for whom? Be specific. "It's a web app for users" is not an answer.

*This system lets the user add course test events and sync them to their google calendars.*

***User action we will trace:** Add an event. The student enters the event details of the event (course, title, and date) and submits them, causing the frontend to send the event data to the backend, where it is stored in the database and returned for display on the calendar.*

## **Part 2: As-built architecture diagram**

Draw boxes and arrows for every major component. Draw only what the code proves exists. Label each arrow with what travels along it (HTTP request, SQL query, event, file).

Include any of these that exist:

* Client (web, mobile, CLI)  
* Server or API layer  
* Database or storage  
* External services and APIs  
* CI/CD pipeline and hosting

**Insert diagram image here.**

\[Web browser: exam form\] \--HTTP POST /events (JSON: course, title, date)-------------------------\> \[Flask API\]

\[Flask API\] \--save exam---------------------------------------------------------------------------------\> \[SQLite: events.db\]

\[Flask API\] \--create event (HTTPS Calendar API request)----------------------------------\> \[Google Calendar API\]

\[Google Calendar API\] \--created event \+ calendar link—-------------------------------------------------\> \[Flask API\]

\[Flask API\] \--JSON response (saved exam, sync status/link)----------------------------------------\> \[Web browser\]

***Example.** Five components, every arrow labeled with what travels on it.*

\[React client\] \--HTTPS POST /api/profiles (JSON \+ JWT)--\> \[Express API\]  
\[React client\] \--image upload (multipart)-------------\> \[Image storage\]  
\[Express API\]  \--verify JWT----------------------------\> \[Auth middleware\]  
\[Express API\]  \--SQL INSERT INTO profiles--------------\> \[PostgreSQL\]  
\[GitHub Actions\] \--build, test, deploy on push to main-\> \[Hosting: client \+ API\]

## **Part 3: Trace the click**

Follow your one user action from the button click to the database and back. Minimum five hops. Every row needs a real file path and function name. Add rows as needed.

**Your trace:**

| Step | Layer | File and function | Data in / data out | Notes or surprises |
| :---- | :---- | :---- | :---- | :---- |
| 1 | Frontend | frontend/[script.js](http://script.js) → addEventListener() → flask.api | Form submit syllabus  → links and opens Google Calendar → handles catches if google isnt synced → sends POST request  |  |
| 2 | Frontend  |  frontend/[script.js](http://script.js) → fetch("http\://127.0.0.1:5000/events") | Submitted exams create a list view for the user.  |  |
| 3 | Backend | [app.py](http://app.py) \- \> create\_event() | JSON request from /events to create an exam object |  |
| 4 | Backend logic | [exam.py](http://exam.py) \-\> Exam.\_\_init\_\_() | Course, title, and date initialized as an Exam object |  |
| 5 | Backend Database | Exam\_database.py \-\>ExamDatabase.save\_exam() | Exam objects gets inserted into the SQLite events table |  |
| 6 | Backend google server | Goog\_calendar\_service.py \-\> GoogleCalendarService.add\_exam() | Saved the Exam object and creates a google calendar event |  |
| 7 | Backend | [app.py](http://app.py)\-\> create\_event() | Saved exam and google calendar Calender result |  |
| 8 |  |  |  |  |

## 

## 

## 

## 

## **Part 4: Reality check and open questions**

Open the handoff UML and compare it to your diagram. Circle every mismatch on your diagram.

**What the handoff docs got wrong or left out:**

1. Flask.API is not listed on the original uml

**Three questions for the original team.** For each, note whether it is about intent ("was this on purpose?") or design ("why is it built this way?").

1. Was it designed to let the user view events before it is added to their calendar. (pdf upload —\> calendar)  
2. Why does the system use a backend when you could just send the course info straight to the calendar?  
3. How does the system handle not having enough information added such as no course name?

   ***Example.***

   ***Mismatches:** (1) The handoff UML shows a separate Interests table, but the code stores interests as a comma-separated string in profiles. (2) The UML never mentions the image storage service.*

   ***Questions for the original team:***

1. Intent: Can one user create more than one profile? The code allows it.  
2. Design: Why are interests a string instead of a join table?  
3. Intent: Is the photo required? The form says optional, but the API rejects a profile without one.

## **Part 5:Candiate requirements**

| ID | Candidate Req | Type | Source  | Status | Acceptance criterion  |
| :---- | :---- | :---- | :---- | :---- | :---- |
| CR-1 | System shall save a submitted exam to the exams table | Functional  | [app.py](http://app.py) \- \> create\_event()[exam.py](http://exam.py) \-\> Exam.\_\_init\_\_() | Confirmed  | POST/ Events with course title, midterm dates returns the saved exam and adds to the list |
| CR-2 | System shall create a Google Calendar event for each exam | Functional | Goog\_calendar\_service.py \-\> GoogleCalendarService.add\_exam() | Confirmed | After POST request response includes a calendar link and the event appears on the calendar  |
| CR-3 | System shall reject an exam with no course name | Functional | Whether Exam.\_\_init\_\_() valadiates anything  | Unconfirmed | POST returns a 400 error message |
| CR-4 | System shall keep an exam while reporting a Google Calendar sync error  | Functional | Check if createevents() throws anything | Bug | After POST request there should be a 201 sync error |
| CR-5 | System shall send requests to a configurable ip address | Non-Functional | frontend/[script.js](http://script.js) → fetch("http\://127.0.0.1:5000/events")  | Unconfirmed | Changing a config changes the URL  |

## **Part 6: three unit test cases**

| ID | Requirement | Kind | Unit under test | input | Expected output | Predicted today |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| TC-1 | CR-1 | Positive  | [exam.py](http://exam.py) \-\> Exam.\_\_init\_\_() | Exam (“CS 250”, “Midterm”, “2026-11-05”)  | Object with 3 attributes stored | Pass |
| TC-2 | CR-3 | Negative | [exam.py](http://exam.py) \-\> Exam.\_\_init\_\_() | Exam (“”, “Midterm”, “2026-11-05”)  | Raises an error | Fails if no validation exists |
| TC-3 | CR-3 | Boundary  | [exam.py](http://exam.py) \-\> Exam.\_\_init\_\_() | Exam (“A”, “Midterm”, “2026-11-05”)  | Object created | pass |

## **Grading checklist**

* ☐ Purpose sentence is specific, not generic  
* ☐ Diagram matches the code, not the handoff docs  
* ☐ Trace has at least five hops, each with a file path  
* ☐ At least one doc-vs-reality mismatch is identified  
* ☐ Three real questions for the original team  
* ☐ Every role has a named owner, and the two trace halves meet at the same endpoint.