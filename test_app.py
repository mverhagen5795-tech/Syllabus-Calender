# Import our Flask app so we can test it
from app import app

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