import anthropic 
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
antwort = client.messages.create (
    model="claude-sonnet-4-6",
    max_tokens=10000,
    messages=[
        {"role":"user", "content": "Was ist RAG? Erklare es in 2 Saetzen."}
    ]
)
print(antwort.content[0].text)
