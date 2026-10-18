# Nächste Schritte (Stand 18.10.2026)

Reihenfolge ist Empfehlung. Jeder Block ist unabhängig, du kannst auch springen.
"Chrome-Claude" = die Claude-Seitenleiste in deinem Chrome. Die Aufträge dafür
stehen jeweils als Kasten zum Kopieren.

## Block A · YouTube am Mac (erledigt für KW 43, ab jetzt wöchentlich)
Stand 18.10.: vier Shorts geplant. Ab jetzt jede Woche am Mac:
1. Reel-Datei aus Edits in die Galerie exportieren, per AirDrop auf den Mac
   (Stimme und Musik bleiben drin, wie am 18.10. geprüft).
2. studio.youtube.com → oben rechts "Erstellen" → "Videos hochladen" → Datei.
   Hochformat unter 3 Minuten wird automatisch als Short erkannt.
3. Titel und Beschreibung aus `youtube/<KW>.md` einfügen. "Nein, nicht für
   Kinder". Weiter, Weiter.
4. Sichtbarkeit "Planen", Datum und Uhrzeit (werktags 18:30, Sonntag 10:00),
   "Planen".
5. Nach der Veröffentlichung: Video in "Inhalte" öffnen → Kommentare →
   Kommentar aus der Batch-Datei schreiben → drei Punkte → "Fixieren".
6. Sonntags: Screenshot "Analytics, letzte 7 Tage" an Claude, dazu die Links
   der neuen Reels der Woche (Chrome-Claude kann sie auslesen). Daraus kommt
   der nächste Batch.

## Block B · Flodesk (Formulare erledigt 18.10., Rest offen)
Formulare /3-tage-plan und /trainingsguide sind live und in den Shorts verlinkt.
Noch offen:
1. Mit eigener E-Mail testen: eintragen, Bestätigungsmail, dann Plan/Guide.
2. **RETTUNG-Workflow erweitern** (Systemcheck: nur 1 Mail, keine Einladung).
   Ich schreibe Mail 2 und Mail 3 als Entwurf in `creatives/`, Selma gibt frei,
   du trägst sie in Flodesk ein (Workflow "7 Familienrezepte" → Schritt
   hinzufügen → Zeitverzögerung 3 Tage → E-Mail; dann 4 Tage → E-Mail).
3. **TAUSCH:** entweder (a) in ManyChat eine Keyword-Automation TAUSCH anlegen,
   die das PDF schickt und zum Flodesk-Formular verlinkt, plus Flodesk-Workflow
   "Tausch-Liste" (1 Mail mit PDF), oder (b) Selma sagt im nächsten Reel ein
   anderes Keyword. Bis dahin verlinken Short 3 und die Shorts-Kommentare den
   Cortisol-Guide.
4. Datenschutz-Link in beiden Flodesk-Formularen: bis Block D erledigt ist
   `https://selmanuhija.com/#datenschutz`, danach `/datenschutz.html`.

## Block C · Meta fertig machen (20 Minuten)
1. Einladung annehmen: Mail an amir.keric@me.com vom Business Portfolio
   bestätigen, oder auf business.facebook.com mit deinem eigenen Facebook-Konto
   anmelden und den Hinweis oben annehmen.
2. Chrome-Claude:
   ```
   business.facebook.com/settings, Portfolio "Selma Nuhija". Vor jeder Änderung bestätigen lassen.
   1. Konten > Seiten > Hinzufügen. Gibt es eine Seite von Selma, diese wählen. Sonst "Neue Seite erstellen", Name "Selma Nuhija", Kategorie "Coach".
   2. Konten > Werbekonten > "Selma Ads" > Assign people > amir.keric@me.com > Full access.
   3. Konten > Instagram-Konten: prüfen, dass @selmanuhija drin ist.
   4. Screenshots von Seiten, Instagram-Konten und People-Ansicht von "Selma Ads".
   ```
3. Screenshots hier in den Chat.
4. Danach Meta-Ads-Connector verbinden (Phase 3 in ANLEITUNG.md):
   - Auf deinem Mac Terminal öffnen: `cd` in den Ordner `Shramba/selma-ads`,
     dann `claude mcp add --transport http meta-ads https://mcp.facebook.com/ads`,
     dann `claude` starten, `/mcp` eingeben, bei meta-ads "Authenticate".
   - Im Browser mit **deinem** Facebook-Konto anmelden, "Opt in for current
     business only", Portfolio "Selma Nuhija".
   - Testen: "Liste die Werbekonten, auf die du Zugriff hast." Es muss
     act_2982640922095203 "Selma Ads" erscheinen.

## Block D · Webseite (10 Minuten + Selma) · **zuerst erledigen**
Stand 18.10. abends: `/datenschutz.html` und `/impressum.html` liefern 404.
Die Flodesk-Formulare sind live, darum ist das der einzige Punkt mit
rechtlichem Zeitdruck.
1. Bei Hitrost einloggen → Dateimanager oder FTP → `impressum.html` und
   `datenschutz.html` aus `selma-ads/website/` ins gleiche Verzeichnis wie
   `index.html` hochladen.
2. Prüfen: selmanuhija.com/datenschutz.html und /impressum.html laden.
3. Selma liest den Entwurf "12. Werbeanzeigen auf Instagram (Meta)" in
   `kunde/webseite.md` und sagt ja oder was geändert werden soll.
4. Nach Freigabe: Abschnitt in `index.html` (Datenschutz, nach Punkt 11) und
   in `datenschutz.html` einfügen, beide hochladen. Ich kann die Dateien
   vorbereiten, sag Bescheid.

## Block E · Zwei Fragen an Selma (5 Minuten)
1. Wie viele Kundinnen hat die Membership aktuell?
2. Wie viele davon kamen über ein Freebie (Reel, Kommentar, Guide)?
Grobe Zahlen reichen. Daran hängt, ob 7 € pro Lead realistisch sind.

## Block F · Erster Wochenlauf (sobald Block C fertig ist)
1. Terminal: `cd Shramba/selma-ads`, `claude`, dann `/wochenlauf`.
2. Claude legt alles pausiert an und zeigt die Zusammenfassung.
3. Du und Selma lest die Anzeigentexte. Dann: `FREIGABE <Kürzel>, Budget 10 €/Tag`.
4. Erst dann läuft Geld.

## Danach, jede Woche
| Wann | Wer | Was |
|---|---|---|
| Mo | du | `/wochenlauf`, lesen, FREIGABE |
| Mi/Fr/So/Mo | du oder Selma | neues Reel auch als Short hochladen, Texte von `/youtube` |
| täglich | Selma | Leads/DMs beantworten |
| Do | du | "Zahlen?" an Claude |
