# AI-Engineering Crashkurs

Ein selbst gebautes RAG-System (Retrieval-Augmented Generation), das Claude mit eigenem Wissen aus einer Datenbank versorgt.

## Problem

Sprachmodelle wie Claude kennen keine internen/eigenen Daten. Um Fragen zu spezifischen Inhalten (z.B. Projektbeschreibungen) zu beantworten, muss das Modell diese Inhalte als Kontext bekommen.

## Architektur

1. **Embeddings** – Texte werden mit `sentence-transformers` in Vektoren (Zahlen) umgewandelt, die ihre Bedeutung abbilden
2. **Speicherung** – Die Vektoren landen in Supabase (PostgreSQL mit pgvector-Erweiterung)
3. **Suche** – Eine SQL-Funktion (`match_dokumente`) findet per Ähnlichkeitssuche die relevantesten gespeicherten Texte zu einer Frage
4. **Antwort** – Die gefundenen Texte werden zusammen mit der Frage an die Anthropic API (Claude) geschickt, die daraus eine fundierte Antwort generiert

## Stack

Python · Anthropic API · Supabase (pgvector) · sentence-transformers

## Ergebnis

Funktionierende End-to-End-Pipeline: Frage stellen → relevante Dokumente werden automatisch gefunden → Claude antwortet basierend auf diesem Kontext.