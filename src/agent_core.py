import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_agent(message: str) -> str:
    """
    Real AI support agent call.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # small + cheap, upgrade later
            messages=[
                {"role": "system", "content": "You are a helpful tech support agent."},
                {"role": "user", "content": message}
            ]
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"[Error from AI engine: {e}]"
