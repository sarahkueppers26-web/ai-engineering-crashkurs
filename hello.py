# 1.Varibale
frage= "was ist RAG"
max_tokens=10000
# 2. Liste 
dokumente = ("Vertrag.pdf", "Ausschreibungen", "Policy.pdf")
# 3. Dictionary 
antwort= {
    "text":"RAG steht fuer Retrieval Augmented Generation",
    "tokens": 42
}
# 4. Funktion
def frage_stellen(frage):
    print("Frage:"+frage)
    return "Antwort kommt gleich"
# 5. If-Abfrage
ergebnis=frage_stellen(frage)
if ergebnis:
    print(antwort["text"])
