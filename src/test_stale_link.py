import pytest

import app as app_module
from src.exam_database import ExamDatabase


class FakeCalendar:
    """Stands in for Google Calendar so tests never hit the real API."""

    def __init__(self):
        self.last_event_link = None
        self.should_succeed = True

    def add_exam(self, exam):
        if self.should_succeed:
            self.last_event_link = "https://calendar.example/first-event"
            return True
        return False


@pytest.fixture
def client(tmp_path, monkeypatch):
    fake = FakeCalendar()
    monkeypatch.setattr(
        app_module, "exam_database", ExamDatabase(str(tmp_path / "test.db"))
    )
    monkeypatch.setattr(app_module, "google_calendar_service", fake)
    app_module.app.config["TESTING"] = True
    return app_module.app.test_client(), fake


def test_failed_sync_does_not_return_previous_link(client):
    http, fake = client

    http.post("/events", json={"course": "CS 250", "title": "Midterm", "date": "2026-12-10"})

    fake.should_succeed = False
    resp = http.post("/events", json={"course": "CS 302", "title": "Final", "date": "2026-12-12"})
    body = resp.get_json()

    assert resp.status_code == 201
    assert body["calendar_added"] is False
    assert "calendar_link" not in body
