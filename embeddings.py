from sentence_transformers import SentenceTransformer
from supabase import create_client
from dotenv import load_dotenv
import os
load_dotenv()
supabase= create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
model=SentenceTransformer("all-MiniLM-L6-v2")
texte=["Microsoft Neue Accounts", "Wir sind dabei neue Microsoft Zugaenge zu besorgen, da die aktuellen Mailadressen zu viel Verwirrugn fuehrt ", "Wir muessen die Nutzung von MeinMVP noch verbessern, speziell den GDV Daten Abgleich"]
for text in texte:
    embedding =model.encode(text).tolist()
    supabase.table("dokumente").insert({
        "inhalt":text,
        "embedding":embedding
    }).execute()
    print (f"Gespeichert:{text}")