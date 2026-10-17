---
name: kampagne
description: Kampagne, Ad Sets und Ads für Selma im Meta-Werbekonto anlegen (immer PAUSED) oder nach FREIGABE aktivieren, Budget setzen, Anzeigen pausieren. Anwenden bei "Kampagne anlegen", "hochladen", "aktivieren", "FREIGABE", "Budget ändern", "pausieren", oder als Schritt 4 im Wochenlauf.
---

# Kampagne

Dieser Skill ist der einzige, der ins Werbekonto schreibt. Die
Freigabe-Schranke aus `CLAUDE.md` gilt hier wörtlich.

## Voraussetzungen prüfen (vor jeder Aktion)
1. Meta-Ads-MCP verbunden und authentifiziert? Wenn nicht: sagen, abbrechen.
   Nie so tun, als wäre etwas angelegt worden.
2. Werbekonto-ID aus `kunde/selma.md` (`act_…`). Nur dieses Konto. Im Chat
   nennen: "Arbeite in act_… (Selma)".
3. Zu jeder Ad: Batch-Datei in `creatives/` mit bestandenem Compliance-Check.
   Ohne Check keine Ad.
4. Funnel aus `kunde/selma.md`: bestimmt Kampagnenziel und CTA.

## Struktur, die angelegt wird
```
Kampagne   SELMA | <Ziel> | <YYYY-WW>          Status: PAUSED
  Ad Set   Kalt – breit | Instagram             Status: PAUSED, Budget: noch nicht gesetzt
    Ad     ERK-1 | Reel 9:16                   Status: PAUSED
    Ad     ALL-2 | Feed 4:5                    Status: PAUSED
  Ad Set   Warm | Instagram                    Status: PAUSED
    Ad     …
```
- **Kampagnenziel** nach Funnel: Leads (Instant Form oder Conversions), oder
  Interaktion/Nachrichten (WhatsApp/DM).
- **Budget:** Campaign Budget Advantage (CBO) auf Kampagnenebene bevorzugen,
  Wert erst mit Freigabe. Beim Anlegen das kleinste technisch nötige Budget
  wählen und den Wert im Chat als "Platzhalter, nicht freigegeben" markieren.
- **Zielgruppen** aus dem Output von `/zielgruppe`.
- **Platzierungen:** manuell, nur Instagram (Reels, Feed, Stories, Explore).
  Vor dem Anlegen prüfen, dass keine Facebook-, Messenger- oder
  Audience-Network-Platzierung aktiv ist. Identität der Anzeige: Instagram-
  Konto @selmanuhija, Facebook-Seite nur als technischer Träger.
- **Instant Form:** vorhandenes Formular von Selma verwenden. Keines da:
  Formular-Entwurf (Felder: Vorname, E-Mail, Telefon optional, eine Frage
  "Was ist gerade deine größte Herausforderung?" als Auswahl) im Chat
  vorschlagen und Datenschutz-URL abfragen. Nicht ohne Datenschutz-URL anlegen.
- **Bilder/Videos:** aus `creatives/` hochladen, wenn Dateien vorhanden.
  Fehlen sie: Ad trotzdem als Entwurf mit Platzhalter beschreiben, im Chat
  auflisten, was Selma noch liefern muss. Keine Stockbilder eigenmächtig.
- Eine bestehende Kampagne der Vorwoche wird nicht gelöscht, sondern läuft
  weiter oder wird pausiert (nach Freigabe).

## Aktivieren nach FREIGABE
Nachricht enthält `FREIGABE` und nennt Ads/Ad Sets und Budget, z. B.
`FREIGABE ERK-1, ALL-2, Budget 15 €/Tag`.
1. Budget gegen das Tageslimit in `CLAUDE.md` prüfen (Summe aller aktiven
   Kampagnen). Darüber: stoppen, nachfragen.
2. Genau die genannten Ads auf ACTIVE, dazugehöriges Ad Set und Kampagne auf
   ACTIVE, Budget setzen.
3. Nicht genannte Ads bleiben PAUSED.
4. Im Chat bestätigen: Tabelle mit ID, Name, Status, Budget, Startzeit.
   Dann in `berichte/YYYY-WW.md` unter "Freigegeben" eintragen.

## Pausieren / Stoppen
- "Pausiere ERK-1" ist eine Aktion, die Kosten senkt, und braucht keine
  Freigabe: sofort ausführen und bestätigen.
- Löschen braucht `FREIGABE`.

## Regeln
- Niemals ACTIVE, Budget, Gebot, Laufzeit, Zielgruppe einer aktiven
  Kampagne ohne `FREIGABE` in der aktuellen Nachricht.
- Keine Advantage+-Shopping/-Sales-Kampagnen, kein Katalog. Hier geht es um
  Leads und Gespräche.
- Nach jedem Schreibvorgang den Zustand aus dem Werbekonto zurücklesen und
  berichten, nicht aus dem Gedächtnis.
- Fehlermeldung von Meta (abgelehnte Anzeige, Richtlinie): Text zitieren,
  Anzeige nicht umschreiben und erneut einreichen, sondern Amir fragen.
