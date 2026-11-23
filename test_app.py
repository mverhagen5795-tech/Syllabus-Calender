# Import our Flask app so we can test it
from app import app
from src.create_exam_timer import CreateExamTimer
from src.display_exam_times import DisplayExamTimes

# REQ-4 test: add an event and check it comes back from /events
def test_req4_add_event_and_see_it():
    client = app.test_client()

    # Send a new event to POST /events 
    client.post("/events", json={"course": "CS 250", "title": "Test Exam", "date": "2026-11-01"})

    # Ask GET /events for all saved events
    response = client.get("/events")
    events = response.get_json()

    # assert = "this must be true". If the event is in the list, the test passes
    assert {"course": "CS 250", "title": "Test Exam", "date": "2026-11-01"} in events


def test_create_exam_timer_constructor():
    end_date = "2026-11-01"

    timer = CreateExamTimer(end_date)

    assert timer.endDate == end_date
    assert timer.startDate is not None


def test_display_exam_times_constructor():
    display = DisplayExamTimes()

    assert display.days == 0
    assert display.hours == 0
    assert display.minutes == 0
# PR4 Bug 1 test: verify Google Calendar failures are communicated
def test_calendar_failure_provides_error_message(monkeypatch):
    client = app.test_client()

    # Simulate Google Calendar insertion failing
    monkeypatch.setattr(
        "app.google_calendar_service.add_exam",
        lambda exam: False
    )

    # Prevent an old successful event link from affecting the test
    monkeypatch.setattr(
        "app.google_calendar_service.last_event_link",
        None
    )

    # Submit an exam
    response = client.post(
        "/events",
        json={
            "course": "CS 250",
            "title": "Calendar Failure Test",
            "date": "2026-12-01"
        }
    )

    result = response.get_json()

    # The exam should still be saved locally
    assert response.status_code == 201
    assert result["calendar_added"] is False

    # The application should explain why calendar insertion failed
    assert result.get("calendar_error")


def test_oauth_callback_redirects_to_home(monkeypatch):
    client = app.test_client()

    # Simulate successful Google authorization
    monkeypatch.setattr(
        "app.google_calendar_service.finish_authorization",
        lambda **kwargs: None
    )

    # Simulate an existing OAuth session
    with client.session_transaction() as session:
        session["oauth_state"] = "test-state"
        session["oauth_code_verifier"] = "test-verifier"

    response = client.get("/oauth2callback")

    assert response.status_code == 302
    assert response.headers["Location"] == "/"

def test_whitespace_only_course_is_rejected():
    client = app.test_client()

    response = client.post(
        "/events",
        json={
            "course": "   ",
            "title": "Midterm",
            "date": "2026-11-05",
        },
    )

    assert response.status_code == 400


def test_invalid_date_is_rejected():
    client = app.test_client()

    response = client.post(
        "/events",
        json={
            "course": "CS 250",
            "title": "Midterm",
            "date": "not-a-date",
        },
    )

    assert response.status_code == 400
