---
name: wochenlauf
description: Der wöchentliche Meta-Ads-Lauf für Selma in einem Stück – Auswertung der Vorwoche, Zielgruppe nachschärfen, neue Creatives, Kampagne pausiert anlegen, Freigabe-Zusammenfassung. Anwenden bei "Wochenlauf", "Montagslauf", "mach die Ads für diese Woche", "weekly run".
---

# Wochenlauf

Führt die vier Skills in fester Reihenfolge aus. Jeder Schritt liest seinen
eigenen SKILL.md. Nichts wird aktiviert; am Ende steht eine
Freigabe-Zusammenfassung.

## Ablauf
0. **Vorbereitung:** Kalenderwoche bestimmen (`YYYY-WW`). Prüfen, ob
   `kunde/selma.md` noch `[…]` an Stellen hat, die diese Woche gebraucht
   werden (Werbekonto-ID, Funnel, Sprache, Link). Fehlt etwas davon:
   Lauf anhalten und die fehlenden Angaben als Liste ausgeben. Fehlen nur
   Nebensächlichkeiten: weiter, am Ende auflisten.
   MCP verbunden? Wenn nicht: nur Schritte 2 und 3 ausführen und das sagen.
1. **/auswertung** → `berichte/YYYY-WW.md`. Erste Woche ohne Daten: Bericht
   mit "Noch keine Daten" anlegen, weiter.
2. **/zielgruppe** → Abschnitt im Bericht, Setup für Schritt 4.
3. **/creatives** → `creatives/YYYY-WW-batch.md`, 3–5 Anzeigen, alle mit
   bestandenem Compliance-Check.
4. **/kampagne** → Kampagne/Ad Sets/Ads anlegen, **alle PAUSED**. Ohne
   Bild-/Videodateien nur die Textteile anlegen und auflisten, was fehlt.
5. **Zusammenfassung für die Freigabe** (im Chat, max. 12 Zeilen):
   ```
   Wochenlauf KW XX – zur Freigabe
   Vorwoche: … € ausgegeben, … Leads, CPL … € (Ziel … €)
   Vorschlag pausieren (ohne Freigabe sofort möglich): …
   Neu angelegt (PAUSED): ERK-1 Reel, ALL-2 Feed, EIN-1 Reel
   Zielgruppe: unverändert / geändert: …
   Budgetvorschlag: … €/Tag (Limit … €)
   Selma muss liefern: Video zu ERK-1 (Briefing in creatives/…), Foto für ALL-2
   Offen in kunde/selma.md: …
   Freigabe-Beispiel: FREIGABE ERK-1, ALL-2, Budget 15 €/Tag
   ```
6. **Stopp.** Warten auf `FREIGABE`. Kommt sie, übernimmt `/kampagne`.

## Regeln
- Reihenfolge nicht ändern, Schritte nicht überspringen (außer MCP fehlt).
- Jeder Schritt schreibt in seine Datei; der Wochenlauf fasst nur zusammen.
- Keine Aktivierung, kein Budget, auch nicht "zum Testen".
