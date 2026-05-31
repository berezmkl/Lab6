"""Tests for the event calendar module."""
import pytest
from src.calendar import add_event, remove_event, get_events, count_events


def test_add_event():
    events = []
    result = add_event(events, "Meeting")
    assert "Meeting" in result


def test_add_empty_event():
    events = []
    with pytest.raises(ValueError):
        add_event(events, "")


def test_remove_event():
    events = ["Meeting", "Lunch"]
    result = remove_event(events, "Meeting")
    assert "Meeting" not in result


def test_remove_nonexistent_event():
    events = ["Meeting"]
    with pytest.raises(ValueError):
        remove_event(events, "Lunch")


def test_get_events():
    events = ["Meeting", "Lunch"]
    result = get_events(events)
    assert result == ["Meeting", "Lunch"]


def test_count_events():
    events = ["Meeting", "Lunch", "Call"]
    assert count_events(events) == 3