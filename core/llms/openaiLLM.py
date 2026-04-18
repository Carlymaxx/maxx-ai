from langchain_openai import ChatOpenAI
import os

def get_llm(model='gpt-4o-mini'):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    llm = ChatOpenAI(model=model, api_key=api_key)
    return llm