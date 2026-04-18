from langchain_anthropic import ChatAnthropic
import os

def get_llm(model='claude-3-haiku-20240307'):
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable not set")
    llm = ChatAnthropic(model=model, anthropic_api_key=api_key)
    return llm