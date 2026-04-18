from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from core.brain import Brain
from utils.stt import GoogleSpeechRecognition
from utils.tts import DeepgramTTS
import threading
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'maxx_ai_secret'
socketio = SocketIO(app)

stt = GoogleSpeechRecognition()
tts = DeepgramTTS(voice='aura-arcas-en')
brain = Brain(agentMode=True)

is_listening = False

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('voice_input')
def handle_voice(data):
    global is_listening
    text = stt.synthesize()
    if text:
        socketio.emit('user_message', {'text': text})
        resp = brain.invoke(text)
        socketio.emit('ai_response', {'text': resp})
        tts.speak(resp)

@socketio.on('text_input')
def handle_text(data):
    text = data.get('text', '')
    if text:
        socketio.emit('user_message', {'text': text})
        resp = brain.invoke(text)
        socketio.emit('ai_response', {'text': resp})
        tts.speak(resp)

@app.route('/api/voices')
def get_voices():
    from utils.tts.voiceManager import get_available_voices
    return jsonify(get_available_voices())

@app.route('/api/voices', methods=['POST'])
def set_voice():
    data = request.json
    voice = data.get('voice', 'aura-arcas-en')
    return jsonify({'status': 'ok', 'voice': voice})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print(f"Maxx-AI Web App running at http://localhost:{port}")
    socketio.run(app, debug=True, port=port)