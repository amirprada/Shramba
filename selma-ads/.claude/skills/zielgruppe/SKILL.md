---
name: zielgruppe
description: Zielgruppe für Selmas Meta-Ads analysieren und ein konkretes Targeting-Setup vorschlagen (Alter, Geschlecht, Standort, Interessen, Platzierungen, Lookalikes). Anwenden bei "Zielgruppe", "Targeting", "wen sollen wir ansprechen", "Audience", oder als Schritt 2 im Wochenlauf.
---

# Zielgruppe

Ziel: ein Targeting-Setup, das Claude im Skill `kampagne` direkt in Ad Sets
umsetzen kann, plus die Begründung in fünf Zeilen.

## Input
1. `kunde/selma.md` lesen (Zielgruppe, Zielmarkt, Funnel, Sprache).
2. Wenn vorhanden: der letzte Bericht in `berichte/` (Aufschlüsselung nach
   Alter, Platzierung, Geschlecht aus der Vorwoche).
3. Wenn das Meta-Ads-MCP verbunden ist: bestehende Custom Audiences und
   Lookalikes im Werbekonto auflisten (Seitenfans, Instagram-Interaktionen,
   Videoaufrufe, Lead-Formular-Öffner, Website-Besucher).

## Vorgehen
1. **Drei Zielgruppen-Ebenen** aufstellen:
   - **Kalt:** Frauen, Alter 35–55, Standort aus `kunde/selma.md`. Bei Meta
     gilt heute: breites Targeting mit Advantage+ Audience schlägt meist enge
     Interessen. Interessen nur als Vorschlag (Signal, keine Einschränkung).
   - **Warm:** Interaktionen mit Selmas Instagram-Konto (365 Tage),
     Reel-Aufrufe ≥ 25 %, Profilbesuche, DM-Starter, Lead-Form-Öffner ohne
     Absenden, Flodesk-Liste als Kundenliste.
   - **Lookalike:** 1–3 % von Leads oder Kundinnen, sobald mindestens
     100 Personen in der Quelle sind. Vorher nicht anlegen.
2. **Platzierungen:** manuell, **nur Instagram**: Reels, Feed, Stories,
   Explore. Keine Facebook-Platzierung, kein Messenger, kein Audience
   Network (siehe CLAUDE.md). Innerhalb von Instagram: Reels zuerst, weil
   Selmas Material Reels sind. Wenn die Vorwoche zeigt, dass eine
   Instagram-Platzierung über 60 % des Budgets frisst und doppelt so teure
   Leads bringt, vorschlagen, sie auszuschließen.
3. **Ausschlüsse:** bestehende Kundinnen und Leads der letzten 30 Tage aus
   den kalten Ad Sets ausschließen, sobald die Listen existieren.
4. **Datenabgleich mit der Vorwoche:** Welche Altersgruppe, welche
   Platzierung, welches Geschlecht hatte die günstigsten Leads? Nur aus
   echten Zahlen, sonst "noch keine Daten".
5. **Nicht verengen auf Basis einer Woche.** Erst ab 2 Wochen und mindestens
   20 Leads pro Vergleichsgruppe eine Änderung vorschlagen.

## Output (im Chat und als Abschnitt im Wochenbericht)
```
## Zielgruppe KW XX
| Ad Set | Zielgruppe | Alter | Standort | Platzierung | Ausschlüsse |
|---|---|---|---|---|---|
| Kalt – breit | Frauen, Advantage+ Audience | 35–55 | … | nur Instagram | Leads 30 T |
| Warm | IG-Interaktion 365 T + Flodesk-Liste | 35–65 | … | nur Instagram | Kundinnen |
Begründung: (max. 5 Zeilen, mit Zahlen aus der Vorwoche oder "noch keine Daten")
Änderung zur Vorwoche: (keine / was und warum)
```

## Regeln
- Alter immer ≥ 18, hier Untergrenze 35 (siehe `kunde/compliance.md`).
- Keine Interessen, die auf Gesundheitszustand schließen lassen (z. B.
  "Diabetes", "Schilddrüse"). Meta hat solche Interessen ohnehin entfernt,
  Claude schlägt sie auch nicht als Umweg vor.
- Keine Zielgruppe anlegen oder ändern ohne den Skill `kampagne` und dessen
  Freigabe-Regeln.
