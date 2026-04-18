import json
import os
from pathlib import Path

class Config:
    def __init__(self, config_path=None):
        if config_path is None:
            config_path = Path.home() / ".maxx_ai" / "config.json"
        self.config_path = config_path
        self._ensure_default()
    
    def _ensure_default(self):
        if not self.config_path.exists():
            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            default_config = {
                "llm": {
                    "provider": "groq",
                    "model": "mixtral-8x7b-32768"
                },
                "tts": {
                    "voice": "aura-arcas-en",
                    "provider": "deepgram"
                },
                "stt": {
                    "provider": "deepgram"
                },
                "assistant": {
                    "name": "Maxx",
                    "wake_word": "maxx",
                    "activation_key": "ctrl+alt+space"
                },
                "features": {
                    "conversation_history": True,
                    "logging": True
                }
            }
            self.save(default_config)
    
    def load(self):
        try:
            with open(self.config_path, 'r') as f:
                return json.load(f)
        except:
            return {}
    
    def save(self, config):
        with open(self.config_path, 'w') as f:
            json.dump(config, f, indent=2)
    
    def get(self, key, default=None):
        return self.load().get(key, default)
    
    def set(self, key, value):
        config = self.load()
        config[key] = value
        self.save(config)

config = Config()