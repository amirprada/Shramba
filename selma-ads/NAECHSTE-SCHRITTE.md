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
0. **Vorher lesen:** `notizen/evergreen-ads-ideen.md` (dauerhafte Kampagne,
   Start mit 5 €/Tag). Entscheiden, was übernommen wird, dann Skills anpassen lassen.
1. Terminal: `cd Shramba/selma-ads`, `claude`, dann `/wochenlauf`.
2. Claude legt alles pausiert an und zeigt die Zusammenfassung.
3. Du und Selma lest die Anzeigentexte. Dann: `FREIGABE <Kürzel>, Budget 10 €/Tag`.
4. Erst dann läuft Geld.

## Block G · Fixes aus Systemcheck 2 (erledigt 18.10. abends)
Alle neun Punkte ausgeführt, Telefonprüfung von Selma gemacht. Rest offen:
- Erweiterte YouTube-Funktionen: Selma macht Video-Selfie oder Ausweis-Foto
  (Studio → Einstellungen → Kanal → Funktionsberechtigung), oder warten.
- Selma liest den neuen START-DM-Text in ManyChat gegen (Automation "Auto-send
  links from comments") und bestätigt den Button-Link fasterwaycoach.com/?aid=selmanuhija.
- 21-Tage Reset: gibt es nicht mehr (geklärt 18.10.). Nur Membership + 28-Tage-Onboarding.

Der ausgeführte Auftrag, zur Doku:

```
Du bist angemeldet als Selma (YouTube Studio, Flodesk, ManyChat). Führe die folgenden Korrekturen aus. Vor jedem Klick auf "Speichern" oder "Publish" kurz zeigen, was gespeichert wird, und auf mein OK warten. Nichts löschen.

A · YOUTUBE STUDIO (studio.youtube.com)
1. Einstellungen → Kanal → Grundlegende Infos: "Land des Wohnsitzes" = Deutschland. Keywords eintragen: abnehmen ab 40, Frauen ab 40, Perimenopause, Wechseljahre, Protein, Krafttraining, Intervallfasten, FASTer Way. Speichern.
2. Einstellungen → Kanal → Funktionsberechtigung: Status von "Erweiterte Funktionen" ansehen. Wenn "Freischalten" angeboten wird: den Weg über Telefon- bzw. Video-/Ausweisprüfung starten und mir sagen, was verlangt wird (Code per SMS an Selmas Nummer, Ausweis-Foto oder Video-Selfie). Nicht selbst abschließen, nur bis zur Stelle gehen, an der Selma gebraucht wird, und Screenshot.
3. Anpassung → Profil → Links: drei Links anlegen, in dieser Reihenfolge:
   "Webseite" → https://selmanuhija.com
   "3-Tage-Plan kostenlos" → https://fancy-wave-35324.myflodesk.com/3-tage-plan
   "Instagram" → https://instagram.com/selmanuhija
   Veröffentlichen.
4. Inhalte → Shorts: bei allen vier geplanten Shorts Details → "Mehr anzeigen" → Videosprache = Deutsch. Speichern. Datum, Uhrzeit, Titel und Beschreibung nicht anfassen.

B · FLODESK (app.flodesk.com)
5. Forms → "/3-tage-plan" bearbeiten: Datenschutz-Hinweis/Link unter dem Button auf https://selmanuhija.com/#datenschutz setzen (so wie es das Cortisol-Formular macht). Publish. Dasselbe für "/trainingsguide".

C · MANYCHAT (app.manychat.com, Instagram @selmanuhija)
6. Automation → Keyword-Automation öffnen, die auf START reagiert. Keyword INFO als weiteres Trigger-Wort hinzufügen (gleiche Antwort). Speichern.
7. Neue Keyword-Automation "30 MINUTEN": Trigger auf Kommentar und DM mit "30 MINUTEN" und "30MINUTEN". Antwort auf den Kommentar: "Schau in deine DMs 💌". DM-Text: "Hier ist dein 30-Minuten-Trainingsguide, trag dich kurz ein und er kommt per Mail: https://fancy-wave-35324.myflodesk.com/trainingsguide". Aufbau wie die PLAN-Automation (gleiche Verzögerung, gleicher Stil). Aktivieren.
8. Neue Keyword-Automation "TAUSCH": gleich aufgebaut, DM-Text: "Meine Tausch-Liste kommt gerade neu. Bis dahin bekommst du hier meinen 3-Tage-Plan mit allen Rezepten: https://fancy-wave-35324.myflodesk.com/3-tage-plan". Aktivieren.
9. Settings → Inbox: Zahl der ungelesenen Nachrichten und das Datum der ältesten ungelesenen notieren. Nichts beantworten.

AUSGABE: Liste 1–9 mit "erledigt" oder "offen, weil …", plus Screenshots von Kanal-Links, Funktionsberechtigung, den beiden neuen ManyChat-Automationen.
```

## Block H · Membership-Mails in Flodesk (erst nach Selmas FREIGABE)
Betrifft die Workflows "7 Familienrezepte", "1600 Kalorien 3 Tage Meal Plan",
"Dein Trainings-Guide", "Cortisol-Guide HOMEPAGE". Entwurf der Mail steht in
`creatives/rettung-folgemails.md` (Mail 3 ist die VIP-Einladung, Mail 2 nur
für RETTUNG). Sobald Selma den Text freigibt, bekommt Chrome-Claude den
Auftrag: je Workflow nach der PDF-Mail "Zeitverzögerung 3 Tage" und dann die
VIP-Mail einfügen, als Entwurf zeigen, nach OK publishen.

## Danach, jede Woche
| Wann | Wer | Was |
|---|---|---|
| Mo | du | `/wochenlauf`, lesen, FREIGABE |
| Mi/Fr/So/Mo | du oder Selma | neues Reel auch als Short hochladen, Texte von `/youtube` |
| täglich | Selma | Leads/DMs beantworten |
| Do | du | "Zahlen?" an Claude |
