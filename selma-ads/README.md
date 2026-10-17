# Selma Ads – Instagram-Ads und YouTube mit Claude Code

Ein System, mit dem Claude Code die Instagram-Ads (über das Meta-Werbekonto,
**keine Facebook-Platzierungen**) und den YouTube-Kanal für
**Selma Nuhija-Kerić, Certified FASTer Way to Fat Loss Coach** als wöchentlichen
Prozess fährt: Zielgruppe analysieren → Creatives erstellen → Kampagne anlegen
(pausiert) → **Freigabe durch Amir/Selma** → auswerten.

Claude gibt nie selbst frei. Alles, was Geld kostet (Status ACTIVE, Budget,
Gebot, Zielgruppe einer laufenden Kampagne), passiert nur nach dem Wort
`FREIGABE` im Chat. Die Regeln dazu stehen in `CLAUDE.md`.

## Ordnerstruktur

| Pfad | Inhalt |
|---|---|
| `CLAUDE.md` | Projektregeln für Claude: Freigabe-Schranke, Budgetgrenzen, Sprache |
| `kunde/selma.md` | Kundenprofil: Angebot, Zielgruppe, Preise, Ton, Funnel. **Platzhalter `[…]` ausfüllen.** |
| `kunde/compliance.md` | Was Meta bei Abnehm-/Gesundheitswerbung verbietet, plus deutsche Regeln |
| `.claude/skills/zielgruppe/` | Zielgruppen-Analyse und Targeting-Vorschlag |
| `.claude/skills/creatives/` | Hooks, Primary Texts, Headlines, Bild-/Reel-Briefings, Compliance-Check |
| `.claude/skills/kampagne/` | Kampagnenstruktur anlegen (pausiert) über den Meta-Ads-MCP |
| `.claude/skills/auswertung/` | Wochenbericht aus den Insights, Kill-/Skalier-Regeln |
| `.claude/skills/wochenlauf/` | Der Montags-Lauf, der alle vier Skills in Reihe ausführt |
| `.claude/skills/youtube/` | YouTube: Shorts aus Reels, lange Videos (Skript, Titel, Beschreibung, Kapitel) |
| `youtube/` | Ein Plan pro Woche (`YYYY-WW.md`) plus Skripte |
| `vorlagen/` | Vorlagen für Wochenbericht und Creative-Batch |
| `berichte/` | Ein Wochenbericht pro Woche (`YYYY-WW.md`) |
| `creatives/` | Ein Batch pro Woche (`YYYY-WW-batch.md`) plus Bild-/Videodateien |

## Einmaliges Setup

### 1. Meta-Seite: Business Manager und Werbekonto
1. Selma braucht ein **Meta Business Portfolio** (business.facebook.com) mit
   ihrer Facebook-Seite, ihrem Instagram-Konto und einem **Werbekonto** mit
   hinterlegter Zahlungsmethode.
2. Amir wird im Business Portfolio als **Admin** oder mindestens als Person
   mit Werbekonto-Zugriff "Kampagnen verwalten" hinzugefügt.
3. **Meta Pixel / Conversions API** auf Selmas Landingpage installieren, falls
   es eine gibt. Ohne Pixel läuft nur die Leads-Variante über Instant Forms
   oder WhatsApp/DM (siehe `kunde/selma.md`).

### 2. Meta-Ads-MCP in Claude anbinden
Meta betreibt seit April 2026 einen eigenen MCP-Connector (`https://mcp.facebook.com/ads`),
der ohne Developer-App und ohne API-Token auskommt. Anmeldung per OAuth.

**In Claude Code (Terminal):**
```bash
claude mcp add --transport http meta-ads https://mcp.facebook.com/ads
claude            # dann /mcp aufrufen und bei meta-ads "Authenticate" wählen
```

**In claude.ai (für Cloud-Sessions wie diese):** Einstellungen → Connectors →
"Custom connector" → URL `https://mcp.facebook.com/ads` → bei Meta anmelden.

Beim OAuth-Dialog **"Opt in for current business only"** wählen und nur Selmas
Business Portfolio freigeben. So kommt Claude an kein anderes Werbekonto.

Wenn der offizielle Connector nicht geht, ist die Alternative der
Community-Server `meta-ads-mcp` von Pipeboard (`pip install meta-ads-mcp`,
braucht einen Pipeboard-Token). Die Skills hier sind so geschrieben, dass sie
mit beiden funktionieren: sie nennen Fähigkeiten ("Insights abrufen",
"Ad Set anlegen"), nicht konkrete Tool-Namen.

### 3. Dieses Projekt öffnen
```bash
cd selma-ads
claude
```
Claude liest `CLAUDE.md` automatisch. Die Skills stehen als `/zielgruppe`,
`/creatives`, `/kampagne`, `/auswertung`, `/wochenlauf` zur Verfügung.

### 4. `kunde/selma.md` ausfüllen
Alles, was mit `[…]` markiert ist. Vor allem: Preis und Startdatum der
nächsten Runde, Link zur Landingpage oder zum WhatsApp-Kanal, Selmas
eigene Worte für den Ton (zwei, drei Instagram-Captions reinkopieren reicht).

## Der Wochenlauf (jeden Montag)

```
/wochenlauf
```

1. **Auswertung** der letzten 7 Tage: Ausgaben, Leads, Kosten pro Lead,
   Hook-Rate, welche Anzeige gewinnt, welche stirbt. Schreibt `berichte/YYYY-WW.md`.
2. **Zielgruppe** nachschärfen: Was sagen die Daten über Alter, Platzierung,
   Interessen? Vorschlag für die nächste Woche.
3. **Creatives**: 3–5 neue Anzeigen als Text + Bild-/Reel-Briefing, jede mit
   Compliance-Check. Schreibt `creatives/YYYY-WW-batch.md`.
4. **Kampagne**: Neue Ads werden im Werbekonto angelegt, **Status PAUSED**.
5. Claude fasst in zehn Zeilen zusammen, was zur Freigabe steht.

Dann Amir oder Selma:
```
FREIGABE ad 1, 2, 4 – Budget 15 €/Tag
```
Erst jetzt schaltet Claude die genannten Anzeigen aktiv und setzt das Budget.

Für einen manuellen Zwischenstand reicht `/auswertung` allein.

## YouTube
Selma will neben Instagram YouTube aufbauen. Der Skill `/youtube` macht zwei
Dinge: jede Woche die Instagram-Reels als Shorts aufbereiten (Titel,
Beschreibung, Freebie-Link statt Keyword) und zweimal im Monat ein langes
Video zu einer Suchfrage planen. YouTube-Ads kommen erst, wenn Instagram-Ads
vier Wochen gelaufen sind.

## Was Claude nie tut
- Eine Anzeige auf Facebook ausspielen. Platzierungen sind immer nur Instagram.
- Eine Anzeige aktivieren oder ein Budget setzen ohne das Wort `FREIGABE`.
- Mehr als das in `CLAUDE.md` eingetragene Tageslimit vorschlagen.
- Etwas über Selmas Programm behaupten, das nicht in `kunde/selma.md` steht.
- Vorher-Nachher-Bilder, Gewichtsversprechen oder Ansprache nach persönlichen
  Merkmalen verwenden (siehe `kunde/compliance.md`). Das führt zu Ablehnung
  der Anzeige und im Wiederholungsfall zur Sperrung des Werbekontos.
