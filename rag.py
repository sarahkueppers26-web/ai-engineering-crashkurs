from sentence_transformers import SentenceTransformer 
from supabase import create_client
from dotenv import load_dotenv
import anthropic 
import os
load_dotenv()
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
model = SentenceTransformer("all-MiniLM-L6-v2")
client = anthropic.Anthropic (api_key=os.getenv("ANTHROPIC_API_KEY"))
frage= "Warum brauche wir neue Microsoft Zugaenge und was muss noch in MeinMVP verbessert werden?"
frage_embeddding= model.encode(frage).tolist()
ergebnis= supabase.rpc("match_dokumente", {
    "query_embedding": frage_embeddding,
    "match_count": 2
}).execute()

kontext= "\n".join([r["inhalt"]for r in ergebnis.data])
antwort= client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1000,
    messages=[{
        "role":"user",
        "content": f"Kontext:\n{kontext}\n\nFrage: {frage}"
    }]
)
print(antwort.content[0].text)

