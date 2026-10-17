---
name: auswertung
description: Wochenbericht für Selmas Meta-Ads aus den Insights erstellen – Ausgaben, Leads, Kosten pro Lead, Hook-Rate, Gewinner und Verlierer, Kill-/Skalier-Empfehlung. Anwenden bei "Auswertung", "wie laufen die Ads", "Bericht", "Zahlen", "Performance", oder als Schritt 1 im Wochenlauf.
---

# Auswertung

Ziel: `berichte/YYYY-WW.md` nach `vorlagen/wochenbericht.md`, mit Zahlen
ausschließlich aus dem Werbekonto.

## Input
1. Meta-Ads-MCP: Insights der letzten 7 Tage (Montag bis Sonntag) für
   Kampagne, Ad Set und Ad. Zusätzlich Aufschlüsselung nach Alter,
   Platzierung, Geschlecht auf Ad-Set-Ebene. Kein MCP: sagen, abbrechen.
2. Vorwochenbericht in `berichte/` für den Vergleich.
3. `kunde/selma.md`: Ziel-Lead-Preis, Budget.

## Kennzahlen (pro Ad, dann aggregiert)
| Kennzahl | Definition | Hinweis |
|---|---|---|
| Ausgaben | spend | |
| Impressionen, Reichweite, Frequenz | | Frequenz > 3 bei kalt = Creative ermüdet |
| Hook-Rate | 3-Sek.-Videoaufrufe / Impressionen | nur Video; < 25 % = Hook schwach |
| Hold-Rate | ThruPlay / 3-Sek.-Aufrufe | |
| CTR (Link) | Link-Klicks / Impressionen | < 0,8 % kalt = Text/Bild überzeugt nicht |
| CPM | | |
| Leads / Nachrichten | je nach Funnel | |
| Kosten pro Lead (CPL) | spend / Leads | Vergleich mit Zielwert aus `kunde/selma.md` |
| Leads mit Antwort | nur wenn Selma Rückmeldung gibt | Qualität schlägt Menge |

## Entscheidungsregeln (Vorschlag, nicht Ausführung)
- **Kill:** Ad hat ≥ 2× Ziel-CPL ausgegeben ohne Lead, oder nach 3 Tagen
  und ≥ 1× Ziel-CPL Ausgaben CTR < 0,5 %. Vorschlag: pausieren.
- **Behalten:** CPL ≤ Zielwert und Frequenz < 3.
- **Skalieren:** CPL ≤ 70 % Zielwert über ≥ 5 Tage und ≥ 10 Leads. Vorschlag:
  Budget um max. 20 % pro Schritt erhöhen, nie verdoppeln.
- **Variieren:** Gewinner-Hook mit neuer Szene/Format in den nächsten Batch
  geben (Input für `/creatives`).
- **Zu früh:** unter 1.000 Impressionen oder < 3 Tage Laufzeit: "zu früh",
  keine Entscheidung.
- Kein Ziel-CPL eingetragen: ersten zwei Wochen nur beobachten und einen
  Zielwert aus dem Median vorschlagen.

## Output
1. Datei `berichte/YYYY-WW.md` nach Vorlage. Vorhandene Datei ergänzen,
   nicht überschreiben.
2. Im Chat, maximal 15 Zeilen:
   - eine Tabelle Ad | Ausgaben | Leads | CPL | CTR | Hook-Rate | Empfehlung
   - drei Sätze: was lief, was stirbt, was kommt
   - Liste der vorgeschlagenen Aktionen mit dem Hinweis, welche davon
     `FREIGABE` brauchen (Budget hoch, Aktivieren) und welche nicht (Pausieren).

## Regeln
- Keine Zahl ohne Quelle aus dem Werbekonto. Fehlt eine Kennzahl: "n/a".
- Keine Aktion ausführen. Pausieren und Aktivieren macht nur `/kampagne`.
- Lead-Qualität: wenn Selma gesagt hat, welche Leads geantwortet oder gebucht
  haben, zählt das mehr als der CPL. Im Bericht getrennt ausweisen.
