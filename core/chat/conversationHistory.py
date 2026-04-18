import json
from pathlib import Path
from datetime import datetime

class ConversationHistory:
    def __init__(self, max_messages=50):
        self.max_messages = max_messages
        self.history_file = Path.home() / ".maxx_ai" / "history.json"
        self._ensure_file()
    
    def _ensure_file(self):
        self.history_file.parent.mkdir(parents=True, exist_ok=True)
        if not self.history_file.exists():
            with open(self.history_file, 'w') as f:
                json.dump({"messages": []}, f)
    
    def load(self):
        try:
            with open(self.history_file, 'r') as f:
                data = json.load(f)
                return data.get("messages", [])
        except:
            return []
    
    def add(self, role, content):
        messages = self.load()
        messages.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })
        if len(messages) > self.max_messages:
            messages = messages[-self.max_messages:]
        with open(self.history_file, 'w') as f:
            json.dump({"messages": messages}, f, indent=2)
    
    def clear(self):
        with open(self.history_file, 'w') as f:
            json.dump({"messages": []}, f)
    
    def get_messages(self):
        return self.load()

conversation_history = ConversationHistory()