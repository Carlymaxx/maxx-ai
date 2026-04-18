import os

AVAILABLE_VOICES = {
    "deepgram": {
        "aura-asteria-en": "Asteria (Female)",
        "aura-arcas-en": "Arcas (Male)",
        "aura-hera-en": "Hera (Female)",
        "aura-zeus-en": "Zeus (Male)",
        "aura-penia-en": "Penia (Female)",
        "aura-orpheus-en": "Orpheus (Male)",
        "aura-apollo-en": "Apollo (Male)",
        "aura-athena-en": "Athena (Female)",
        "aura-luna-en": "Luna (Female)",
        "aura-orion-en": "Orion (Male)",
    },
    "google": {
        "en-US": "English (US)",
        "en-GB": "English (UK)",
        "en-AU": "English (Australia)",
    },
    "elevenlabs": {
        "Rachel": "Rachel (Female)",
        "Adam": "Adam (Male)",
        "Aria": "Aria (Female)",
        "Arnold": "Arnold (Male)",
    }
}

def get_available_voices(provider="deepgram"):
    return AVAILABLE_VOICES.get(provider, {})

def get_voice_by_name(name):
    for provider, voices in AVAILABLE_VOICES.items():
        for voice_id, display_name in voices.items():
            if display_name.lower() == name.lower():
                return provider, voice_id
    return None, None

voice_manager = type('VoiceManager', (), {
    'available': AVAILABLE_VOICES,
    'get_available': get_available_voices,
    'get_voice_by_name': get_voice_by_name
})()