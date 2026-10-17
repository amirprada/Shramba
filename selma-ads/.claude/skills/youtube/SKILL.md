---
name: youtube
description: YouTube für Selma – wöchentlich die Instagram-Reels als Shorts aufbereiten (Titel, Beschreibung, Hashtags, angepinnter Kommentar mit Freebie-Link) und zweimal im Monat ein langes Video planen (Suchfrage, Skript, Titel, Beschreibung, Kapitel, Thumbnail-Text). Anwenden bei "YouTube", "Shorts", "langes Video", "Videoskript", "Kanalbeschreibung".
---

# YouTube

Kein Geld, keine Freigabe-Schranke nötig: Claude schreibt Texte und Pläne,
hochladen tun Amir oder Selma. Schreibt pro Woche eine Datei
`youtube/YYYY-WW.md`.

## Input
1. `kunde/selma.md` (Angebot, Freebies, Ton, Freebie-Seiten auf der Webseite).
2. `kunde/compliance.md`: Gilt auch organisch. YouTube sperrt Videos mit
   Vorher-Nachher-Fokus oder Diätversprechen seltener als Meta, aber die
   Regeln für Anzeigen später sind dieselben. Lieber jetzt sauber bleiben.
3. Der aktuelle Reels-Plan (Amir nennt die Reels der Woche oder verlinkt sie).
4. Wenn vorhanden: YouTube-Studio-Zahlen der Vorwoche (Aufrufe, Wiedergabedauer,
   Abos, Klicks auf Links), von Amir eingefügt.

## Teil A: Shorts (jede Woche, 4 Stück)
Für jedes Reel der Woche:
- **Titel** (max. 60 Zeichen): die Hook-Worte, ohne Hashtag-Wüste. Beispiel:
  "Kartoffeln machen dick? Beide Teller haben 200 kcal"
- **Beschreibung** (3–5 Zeilen): erste Zeile = Hook, zweite = Freispruch,
  dritte = was das Freebie liefert, vierte = Link zur Freebie-Seite,
  dann 3 Hashtags (#abnehmenab40 #frauenab40 #shorts).
- **Angepinnter Kommentar:** ein Satz + Link. "Die 7 Gerichte, bei denen alle
  dasselbe essen, gibt's hier: selmanuhija.com/rettung"
- **Hinweis zur Datei:** Original ohne Instagram-Wasserzeichen, Hochformat 9:16,
  unter 60 Sekunden. Keyword-Einblendung ("Schreib RETTUNG") kann bleiben, es
  schadet nicht, aber der Link ist der Weg.
- Fehlt die Freebie-Seite auf der Webseite: Link auf selmanuhija.com setzen
  und in "Offen" vermerken.

## Teil B: lange Videos (zwei pro Monat, Planung in der ersten Woche des Monats)
1. **Thema wählen** aus den acht Alltagsproblemen und den Mythos-Reels. Kriterium:
   Formuliert als Frage, die eine Frau bei YouTube eintippt. Beispiele:
   "Warum nehme ich ab 40 nicht ab, obwohl ich gesund esse?",
   "Intervallfasten ab 40: welches Fenster passt zu dir?",
   "Warum nimmt mein Mann schneller ab als ich?",
   "Was ich mit Mitte 40 an einem Tag esse, um Fett zu verlieren".
   Nicht zwei Videos zum selben Problem im selben Monat.
2. **Skript** (8–12 Minuten, 1.100–1.600 Wörter gesprochen), Aufbau:
   - 0:00–0:30 Hook: ihr Satz wörtlich, dann das Versprechen des Videos.
     Kein "Hallo ihr Lieben", kein Intro.
   - 0:30–1:30 Freispruch: warum es nicht an der Disziplin liegt.
   - 1:30–8:00 drei bis vier Abschnitte, jeder mit einer konkreten Szene
     (Teller, Küche, Hanteln), jeder endet mit einem Satz, den man sich merkt.
   - 8:00–9:30 Was sie heute tun kann (eine Sache, nicht fünf).
   - 9:30–Ende CTA: Freebie-Link in der Beschreibung, dann Mitgliedschaft in
     einem Satz ohne Preis. Preis steht auf der Webseite.
   Sprache: Selmas Du, kurze Sätze, keine Fachbegriffe ohne Erklärung,
   Zahlen immer mit "ca.".
3. **Titel** (max. 60 Zeichen, Suchbegriff vorn), **Beschreibung** (erste zwei
   Zeilen = Hook + Link, dann Kapitel mit Zeitmarken, dann Freebie- und
   Webseiten-Links, dann 3–5 Hashtags), **Kapitel** (5–7), **Thumbnail-Text**
   (max. 4 Wörter, Selmas Gesicht + ein Teller oder ein Satz).
4. **Drehliste:** welche Szenen Selma filmen muss, in Reihenfolge, mit
   Dauer. Ziel: beide Videos des Monats an einem Drehtag.

## Teil C: Auswertung (wenn Zahlen da sind)
- Shorts: Aufrufe, gesehener Anteil, Abos pro Short. Gewinner-Hooks in den
  nächsten Reels-Plan zurückspielen.
- Lange Videos: Klickrate des Thumbnails (Ziel > 4 %), durchschnittliche
  Wiedergabedauer (Ziel > 40 %), Klicks auf Freebie-Link.
- Kein Zahlenerfinden. Fehlen Zahlen: "noch keine Daten".

## Output
Datei `youtube/YYYY-WW.md` mit Abschnitten "Shorts der Woche", "Langes Video
(wenn fällig)", "Offen". Im Chat: Tabelle Tag | Short-Titel | Freebie-Link,
plus drei Zeilen, was Selma drehen muss.

## Regeln
- Keine Fakten über das Programm, die nicht in `kunde/selma.md` stehen.
- Kein Vorher-Nachher, keine Kilo-Versprechen, keine Krankheitsversprechen.
- Jedes Video endet mit genau einem nächsten Schritt.
