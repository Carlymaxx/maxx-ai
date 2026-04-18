import { useState } from 'react';

export default function Home() {
  const [messages, setMessages] = useState<{role: string, content: string}[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim() || loading) return;
    
    const userMsg = input;
    setInput('');
    setMessages(prev => [...prev, { role: 'user', content: userMsg }]);
    setLoading(true);
    
    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userMsg })
      });
      const data = await res.json();
      setMessages(prev => [...prev, { role: 'ai', content: data.response }]);
    } catch (e) {
      setMessages(prev => [...prev, { role: 'ai', content: 'Error connecting to API' }]);
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 via-blue-900 to-black flex items-center justify-center p-4">
      <div className="max-w-md w-full bg-white/10 backdrop-blur-lg rounded-3xl p-8 shadow-2xl">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold bg-gradient-to-r from-cyan-400 to-purple-500 bg-clip-text text-transparent">
            Maxx-AI
          </h1>
          <p className="text-gray-400 mt-2">Voice Assistant Web App</p>
        </div>
        
        <div className="bg-black/30 rounded-xl p-4 h-64 mb-4 overflow-y-auto">
          {messages.length === 0 ? (
            <p className="text-gray-300 text-center">Ready to chat...</p>
          ) : (
            messages.map((m, i) => (
              <div key={i} className={`mb-2 p-2 rounded-lg ${m.role === 'user' ? 'bg-cyan-500/30 ml-auto max-w-[80%]' : 'bg-purple-500/30 mr-auto max-w-[80%]'}`}>
                {m.content}
              </div>
            ))
          )}
        </div>
        
        <div className="flex gap-2">
          <input 
            type="text" 
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
            placeholder="Type a message..."
            className="flex-1 bg-white/10 border border-white/20 rounded-xl px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:border-cyan-400"
          />
          <button 
            onClick={sendMessage}
            disabled={loading}
            className="bg-gradient-to-r from-cyan-500 to-purple-500 px-6 py-3 rounded-xl font-semibold hover:opacity-90 transition disabled:opacity-50"
          >
            {loading ? '...' : 'Send'}
          </button>
        </div>
        
        <p className="text-center text-gray-500 text-sm mt-4">
          API keys required in environment variables
        </p>
      </div>
    </div>
  );
}