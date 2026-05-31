"""Simple event calendar module."""


def add_event(events: list, event: str) -> list:
    """Add an event to the calendar."""
    if not event:
        raise ValueError("Event cannot be empty")
    events.append(event)
    return events


def remove_event(events: list, event: str) -> list:
    """Remove an event from the calendar."""
    if event not in events:
        raise ValueError("Event not found")
    events.remove(event)
    return events


def get_events(events: list) -> list:
    """Return all events."""
    return events


def count_events(events: list) -> int:
    """Return the number of events."""
    return len(events)