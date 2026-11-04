---
name: odoo-kontakt
description: Kontakte aus Fotos von Notizen, Visitenkarten oder E-Mail-Signaturen erfassen und in Odoo (https://www.ols-bio.com/odoo/contacts) einpflegen. Zwei Phasen: "erfassen" (vom Handy in der Cloud, Fotos → Eingabedatei im Repo, kein Browser nötig) und "einpflegen" (am Laptop mit Claude in Chrome: prüfen ob Kontakt existiert, sonst anlegen, Notiz loggen, Aktivität planen). Anwenden bei "Notizen erfassen", "in Odoo anlegen", "Kontakt einpflegen", "Aktivität anlegen", "gibt es den schon in Odoo", "Messe-Notizen nach Odoo".
---

# Odoo-Kontakt: erfassen und einpflegen

Amir (Global Product Manager, OLS OMNI Life Science) fotografiert nach Messen,
Besuchen, Calls oder Demos seine Notizen mit dem Handy. Der Skill läuft in zwei
Phasen, die über das Repo zusammenarbeiten:

| Phase | Wo | Braucht | Ergebnis |
|---|---|---|---|
| **1 Erfassen** | Handy, Cloud-Sitzung | nur die Fotos | Eingabedatei `eingaben/<datum>-<anlass>.md`, committet und gepusht |
| **2 Einpflegen** | Laptop, Desktop-App mit Claude in Chrome | Chrome mit Odoo-Login | Kontakte, Notizen und Aktivitäten in Odoo; Bericht in der Eingabedatei, committet und gepusht |

Welche Phase gemeint ist, ergibt sich aus dem Auftrag und der Umgebung: Fotos
im Auftrag und keine Chrome-Werkzeuge = Phase 1. „Einpflegen“, „nach Odoo“ oder
Chrome verbunden = Phase 2. Im Zweifel beide Phasen nacheinander, sofern Chrome
verbunden ist; sonst Phase 1 und am Ende sagen, dass Phase 2 am Laptop folgt.

Leitprinzip: **nichts erfinden, nichts doppelt anlegen, nichts löschen.**

---

# Phase 1 – Erfassen (Handy / Cloud)

Kein Browser nötig. Nie versuchen, aus der Cloud Odoo zu erreichen.

1. Vor dem Start `git pull` auf dem aktuellen Branch, damit keine Eingabedatei
   überschrieben wird.
2. Fotos lesen und Kontakte nach den **Extraktionsregeln** unten herausziehen.
3. Eingabedatei anlegen: `.claude/skills/odoo-kontakt/eingaben/<YYYY-MM-DD>-<anlass>.md`
   nach `vorlage.md`, mit dieser Kopfzeile:
   ```
   status: offen
   anlass: <Messe/Besuch/Call – Ort>   (fehlt es in den Notizen: "[ergänzen]")
   datum: <YYYY-MM-DD>                  (Datum der Fotos / des Auftrags)
   ```
4. Alles Unsichere mit `[?]` markieren, Fragen an Amir unter „Offene Fragen“
   am Ende der Datei sammeln. Wenn Amir im Chat antwortet, die Datei
   nachziehen und die `[?]` entfernen.
5. Committen und pushen (Commit-Text: „odoo-kontakt: <anlass> erfasst, N Kontakte“).
6. Im Chat kurz: Anzahl Kontakte, offene Fragen, und der Hinweis
   „Zum Einpflegen am Laptop: Shramba öffnen, git pull, dann /odoo-kontakt einpflegen“.

## Extraktionsregeln (gelten in beiden Phasen)
Material: Fotos handschriftlicher Notizen, Visitenkarten, Stichpunkte,
E-Mail-Signaturen, Teilnehmerlisten. Die Vorlage in `vorlage.md` nutzen.

Pro Person festhalten:
- **Name** (Vor- und Nachname), Titel (Dr./Prof.) falls lesbar
- **Firma/Institut**, Abteilung, Standort (Ort, Land)
- **E-Mail**, Telefon, Position
- **Sprache** des Kontakts (DE/EN/…), falls aus Material oder Domain ableitbar
- **Anlass** (Messe, Besuch, Call, Demo) und **Datum**
- **Gesprächsnotiz**: Bedarf, Produkte, Zahlen, Zusagen, offene Punkte. Wortlaut
  aus den Notizen übernehmen, nicht ausschmücken.
- **Nächster Schritt** → wird zur Aktivität (Typ, Fälligkeit, Zusammenfassung)

Regeln beim Lesen:
- Unsichere Lesart mit `[?]` markieren, z. B. `Arno[?] Krieger`. E-Mail-Adressen
  sind die wichtigste Dublettenprüfung: Domain und Schreibweise genau prüfen
  (Unidomains, Firmendomains). Unleserlich = `[unleserlich]`, nicht raten.
- Personen ohne jeden Anhaltspunkt für Name **oder** E-Mail werden nicht
  angelegt, sondern nur im Bericht als "nicht anlegbar" aufgeführt.
- Mehrere Personen derselben Firma: Firma einmal, Personen darunter.

---

# Phase 2 – Einpflegen (Laptop / Chrome)

Alle Eingabedateien mit `status: offen` abarbeiten, älteste zuerst, es sei denn
Amir nennt eine bestimmte Datei. Vorher `git pull`.

## Voraussetzungen (vor jeder Aktion prüfen)
1. **Claude in Chrome ist verbunden.** Werkzeuge in einem ToolSearch laden:
   `select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__form_input,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__tabs_close_mcp`
   Wenn die Chrome-Werkzeuge fehlen oder nicht antworten: sagen, dass die
   Browser-Erweiterung nicht verbunden ist, und stattdessen nur Phase 1
   (Erfassen) ausführen. **Nie so tun, als wäre etwas in Odoo angelegt.**
2. `tabs_context_mcp` aufrufen, dann einen **neuen Tab** öffnen und
   `https://www.ols-bio.com/odoo/contacts` laden. Amir ist dort eingeloggt.
   Erscheint die Login-Maske, Amir bitten, sich einzuloggen, und warten.
   Keine Passwörter eingeben oder erfragen.
3. Nur die Kontakte-App und den Chatter benutzen. Keine anderen Odoo-Apps,
   keine Einstellungen, keine Massenaktionen, kein Löschen, kein Archivieren,
   kein Zusammenführen.

**Freigabe vor dem Schreiben:** Die extrahierte Tabelle (Name · Firma · E-Mail ·
geplante Aktivität · Unsicherheiten) kurz zeigen. Einträge ohne `[?]` dürfen
danach direkt angelegt werden. Einträge mit `[?]` in Name, Firma oder E-Mail
erst anlegen, wenn Amir die Lesart bestätigt hat; bis dahin überspringen und im
Bericht als "wartet auf Bestätigung" führen. Hat Amir im Auftrag bereits
"direkt anlegen" gesagt, gilt das nur für Einträge ohne `[?]`.

## Schritt 2 – In Odoo prüfen, ob der Kontakt existiert
Reihenfolge je Person, in der Kontakte-App:
1. **E-Mail** in die Suchleiste tippen und den Vorschlag „E-Mail durchsuchen /
   Search Email" wählen. Treffer = existiert.
2. Kein Treffer: **Nachname** suchen (Vorschlag „Kontakt durchsuchen"). Treffer
   mit passender Firma = existiert. Gleicher Name, andere Firma = neuer Kontakt
   anlegen, im Bericht auf die Namensgleichheit hinweisen.
3. **Firma/Institut** suchen (auch Kurzformen: „Uni Bielefeld" vs. „Universität
   Bielefeld", „Radboudumc" vs. „Radboud"). Ergebnis merken: Firma vorhanden oder
   neu anzulegen.
4. Archivierte Kontakte nicht reaktivieren; falls Odoo einen archivierten
   Treffer anzeigt, im Bericht nennen und Amir entscheiden lassen.

Nach jeder Suche die Suchleiste leeren (Filter-Chip entfernen), sonst bleiben
Filter aktiv und die nächste Suche liefert falsche Ergebnisse.

## Schritt 3 – Fehlende Firma und Kontakt anlegen
Firma zuerst, dann Person.

**Firma (nur wenn nicht vorhanden):** „Neu" → Typ **Unternehmen** → Name exakt
(offizieller Name, z. B. „Bayer AG", „University of Cambridge"), Website falls
bekannt, Ort/Land. Speichern.

**Person:** „Neu" → Typ **Einzelperson** → Name → Feld „Unternehmen" mit der
Firma verknüpfen (Autovervollständigung, bestehenden Eintrag wählen, nicht
„Erstellen" tippen, wenn die Firma schon da ist) → Position → E-Mail → Telefon →
Sprache im Reiter „Verkauf & Einkauf" (nur wenn bekannt). Speichern (Wolken-
Symbol oder Formular verlassen; prüfen, dass kein rotes Pflichtfeld offen ist).

Erfolgskontrolle: Nach dem Speichern steht die URL auf einer Datensatz-ID
(`…/contacts/<id>`), die ID in den Bericht übernehmen.

Bestehende Kontakte **nicht überschreiben**. Fehlt dort die E-Mail oder Position
und das Material liefert sie, ergänzen und im Bericht vermerken. Abweichende
Daten (andere E-Mail, andere Firma) nicht ändern, sondern melden.

## Schritt 4 – Notiz loggen und Aktivität planen
Im Chatter des Kontakts (bei Firmen-Gesprächen ohne klare Person: im Chatter der
Firma):

**Notiz („Notiz hinterlassen / Log note")**, Format:
```
<Anlass>, <Datum> – <Ort/Messe>
Bedarf/Thema: …
Produkte: …
Zahlen/Konditionen: … (nur wenn im Material)
Zusagen/Offen: …
Weitere Personen im Gespräch: …
```
Nur Inhalte aus dem Material. Unsicheres mit `[?]`. Keine Bewertungen der
Person. Mit „Protokollieren / Log" bestätigen (nicht „Senden" – das würde eine
E-Mail an den Kontakt schicken).

**Aktivität („Aktivität planen / Activities")**:
- Typ: `E-Mail` für Angebot/Infos schicken, `Anruf` für Nachfassen, `Besprechung`
  für Termin, `Zu erledigen` für alles andere.
- Zusammenfassung: Verb + Objekt, z. B. „Angebot FBS/MEM 20–40 L schicken",
  „Demo CASYvivo terminieren".
- Fällig: aus dem Material; sonst Standard **+7 Tage** (Messe-Follow-up) bzw.
  **+2 Tage** (Zusage „schicke ich Ihnen"). Zugewiesen an Amir.
- Notiz der Aktivität: ein Satz Kontext. Mit „Planen / Schedule" bestätigen.

Pro Kontakt genau **eine** offene Aktivität anlegen. Hat der Kontakt bereits eine
offene Aktivität zum selben Thema, keine zweite anlegen, sondern melden.

## Schritt 5 – Bericht und Abschluss
Tabs schließen, die der Skill geöffnet hat. Dann in der Eingabedatei:
`status: eingepflegt` setzen (bei Resten mit `[?]`: `status: teilweise`) und am
Ende einen Abschnitt `## Bericht <YYYY-MM-DD>` mit dieser Tabelle anhängen:

| Kontakt | Firma | Status | Odoo-ID | Notiz | Aktivität |
|---|---|---|---|---|---|
| Jasmine Phan | Bayer AG (Berkeley) | neu angelegt | 1234 | ja | E-Mail, fällig 11.11. |
| … | … | bestand bereits | 987 | ja | Anruf, fällig 09.11. |
| … | … | wartet auf Bestätigung `[?]` | – | – | – |

Darunter: offene Punkte (unleserliche Stellen, Namensgleichheiten, Kontakte
ohne E-Mail, abweichende Daten in Odoo). Oder „Nichts offen.“

Committen und pushen (Commit-Text: „odoo-kontakt: <anlass> eingepflegt, N neu,
M bestanden“). Dieselbe Tabelle im Chat zeigen.

## Abbruchregeln
- Browser antwortet nach 2–3 Versuchen nicht, Seite lädt nicht, Element
  reagiert nicht: stoppen, Stand berichten, nicht weiterklicken.
- Odoo zeigt einen Bestätigungsdialog (Löschen, Verwerfen, Zusammenführen):
  **Abbrechen** wählen. Solche Aktionen sind nicht Teil dieses Skills.
- Zweifel, ob ein Treffer dieselbe Person ist: nicht anlegen, fragen.
