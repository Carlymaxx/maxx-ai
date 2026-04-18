import json
import os
from datetime import datetime, timedelta
from pathlib import Path

class CalendarTool:
    def __init__(self):
        self.events_file = Path.home() / ".maxx_ai" / "events.json"
        self._ensure_file()

    def _ensure_file(self):
        self.events_file.parent.mkdir(parents=True, exist_ok=True)
        if not self.events_file.exists():
            with open(self.events_file, 'w') as f:
                json.dump([], f)

    def _load_events(self):
        with open(self.events_file, 'r') as f:
            return json.load(f)

    def _save_events(self, events):
        with open(self.events_file, 'w') as f:
            json.dump(events, f, indent=2)

    def add_event(self, title, date_str, time_str=None, description=""):
        events = self._load_events()
        event = {
            "id": len(events) + 1,
            "title": title,
            "date": date_str,
            "time": time_str,
            "description": description
        }
        events.append(event)
        self._save_events(events)
        return f"Event '{title}' added for {date_str}"

    def list_events(self, date_str=None):
        events = self._load_events()
        if date_str:
            events = [e for e in events if e.get("date") == date_str]
        if not events:
            return "No events found"
        return "\n".join([f"- {e['title']} ({e['date']} {e.get('time', '')}): {e.get('description', '')}" for e in events])

    def remove_event(self, event_id):
        events = self._load_events()
        events = [e for e in events if e.get("id") != event_id]
        self._save_events(events)
        return f"Event {event_id} removed"

calendar_tool = CalendarTool()