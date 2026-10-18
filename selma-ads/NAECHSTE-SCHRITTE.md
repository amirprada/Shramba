# Nächste Schritte (Stand 18.10.2026)

Reihenfolge ist Empfehlung. Jeder Block ist unabhängig, du kannst auch springen.
"Chrome-Claude" = die Claude-Seitenleiste in deinem Chrome. Die Aufträge dafür
stehen jeweils als Kasten zum Kopieren.

## Block A · YouTube starten (heute, 30 Minuten)
1. Originaldateien der vier Reels besorgen, ohne Instagram-Wasserzeichen:
   CapCut-Export oder Galerie auf Selmas Handy. Reels vom 14.10., 06.10.,
   11.10., 08.10.
2. studio.youtube.com → "Erstellen" → "Videos hochladen" → Datei wählen.
3. Titel + Beschreibung aus `youtube/2026-43.md` einfügen. "Nicht für Kinder".
4. Sichtbarkeit "Planen": Mo 19.10. 18:30 / Mi 21.10. 18:30 / Fr 23.10. 18:30 /
   So 25.10. 10:00. Speichern.
5. Video in der Liste öffnen → Kommentar aus der Datei schreiben → drei Punkte
   → "Fixieren".
6. Für alle vier wiederholen. Fertig.

## Block B · Flodesk-Formulare (Chrome-Claude, 15 Minuten)
1. Auftrag aus dem Chat ("app.flodesk.com, angemeldet als Selma. Zwei Full
   page-Formulare …") in die Seitenleiste kopieren.
2. Die beiden Links, die er am Ende ausgibt, hier in den Chat schicken.
3. Mit eigener E-Mail testen: eintragen, Bestätigungsmail, dann Plan/Liste.
4. Ich ersetze die Platzhalter in `youtube/2026-43.md`; du tauschst die Links in
   den YouTube-Beschreibungen und Kommentaren von Short 1 und 3 aus.

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

## Block D · Webseite (10 Minuten + Selma)
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
