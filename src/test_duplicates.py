import pytest

import app as app_module
from src.exam_database import ExamDatabase


class FakeCalendar:
    """Stands in for Google Calendar so tests never hit the real API."""

    def __init__(self):
        self.calls = 0
        self.last_event_link = None

    def add_exam(self, exam):
        self.calls += 1
        self.last_event_link = "https://calendar.example/event"
        return True


@pytest.fixture
def client(tmp_path, monkeypatch):
    fake = FakeCalendar()
    monkeypatch.setattr(
        app_module, "exam_database", ExamDatabase(str(tmp_path / "test.db"))
    )
    monkeypatch.setattr(app_module, "google_calendar_service", fake)
    app_module.app.config["TESTING"] = True
    return app_module.app.test_client(), fake


def test_duplicate_exam_is_not_created_twice(client):
    http, fake = client
    payload = {"course": "CS 250", "title": "Midterm", "date": "2026-12-10"}

    first = http.post("/events", json=payload)
    second = http.post("/events", json=payload)

    assert first.status_code == 201
    assert second.status_code == 409
    assert len(http.get("/events").get_json()) == 1
    assert fake.calls == 1
