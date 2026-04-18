import { NextResponse } from 'next/server';
import Groq from 'groq-sdk';

export async function POST(request: Request) {
  try {
    const { message } = await request.json();
    
    if (!process.env.GROQ_API_KEY) {
      return NextResponse.json(
        { response: "API key not configured. Please set GROQ_API_KEY in Vercel environment variables." },
        { status: 500 }
      );
    }

    const client = new Groq({
      apiKey: process.env.GROQ_API_KEY
    });

    const completion = await client.chat.completions.create({
      model: "mixtral-8x7b-32768",
      messages: [
        {
          role: "system",
          content: "You are Maxx-AI, a helpful AI voice assistant. Keep responses concise."
        },
        {
          role: "user",
          content: message
        }
      ],
      temperature: 0.7,
      max_tokens: 1024
    });

    const response = completion.choices[0]?.message?.content || "No response";
    
    return NextResponse.json({ response });
  } catch (error) {
    return NextResponse.json(
      { response: `Error: ${error instanceof Error ? error.message : 'Unknown error'}` },
      { status: 500 }
    );
  }
}