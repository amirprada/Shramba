# Anleitung für Amir: Selmas Meta-Ads von null aufbauen

Du hast mit Meta-Werbung noch nicht gearbeitet. Diese Anleitung geht davon
aus, dass du nur Selmas Instagram (@selmanuhija) und ihre Webseite
(selmanuhija.com) kennst. Sie ist in Phasen gegliedert. Erst wenn eine Phase
abgehakt ist, kommt die nächste. Ab Phase 3 übernimmt Claude Code die Arbeit,
du gibst nur noch frei.

Meta benennt Menüpunkte regelmäßig um. Wenn ein Begriff hier nicht exakt
passt, such nach dem ähnlichsten. Die Reihenfolge und die Logik bleiben gleich.

---

## Die Begriffe, die du brauchst (5 Minuten)

| Begriff | Was es ist | Bei Selma |
|---|---|---|
| **Facebook-Seite** | Technischer Träger des Werbekontos. Ohne Seite keine Instagram-Anzeige. Es wird nichts auf Facebook ausgespielt. | Hat sie eine? Prüfen. |
| **Instagram-Konto** | Ihr Profil @selmanuhija. Muss ein **Professional-Konto** (Business oder Creator) sein und mit der Facebook-Seite verknüpft. | Verifiziert, 7.154 Follower, Reels vorhanden. |
| **Business Portfolio** (früher Business Manager) | Die Verwaltungsebene darüber, auf business.facebook.com. Hier hängen Seite, Instagram, Werbekonto, Pixel und die Personen mit Zugriff. | Muss auf Selmas Namen laufen. |
| **Werbekonto** | Das "Konto", von dem Anzeigen bezahlt werden. Hat eine ID `act_…` und eine Zahlungsmethode. | Neu anlegen oder vorhandenes prüfen. |
| **Werbeanzeigenmanager** (Ads Manager) | Die Oberfläche, in der Kampagnen gebaut werden. Claude macht das später über den MCP. | adsmanager.facebook.com |
| **Kampagne → Anzeigengruppe → Anzeige** | Die drei Ebenen. Kampagne = Ziel (z. B. Leads). Anzeigengruppe = Zielgruppe, Platzierung, Budget. Anzeige = Text + Video. | Claude legt alle drei an. |
| **Pixel / Datensatz** | Ein Code-Schnipsel auf der Webseite, der Meta meldet, wer die Seite besucht oder sich anmeldet. | Nur nötig, wenn die Webseite Teil des Funnels ist. |
| **Instant Form** | Formular direkt in der Anzeige (Name, E-Mail, Telefon). Kein Pixel nötig. | Guter Start für Selma. |
| **Funnel** | Der Weg von "sieht Anzeige" bis "wird Kundin". | Noch zu entscheiden, siehe Phase 2. |

---

## Phase 1: Zugänge prüfen und dich hinzufügen (Selma + du, ca. 30 Minuten)

Selma hat schon ein Facebook-Konto, ein Business-Konto bei Meta und ihr
Instagram. Es muss also nichts neu angelegt werden, nur geprüft und
freigegeben. Ziel: Du arbeitest in ihrem Werbekonto, ohne ihr Passwort.

### 1.0 Business Portfolio anlegen (einmalig, 10 Minuten)
Stand 17.10.: Das Werbekonto act_956540482250069 ist ein persönliches Konto
ohne Portfolio. Im Ads Manager im Konto-Dropdown auf **"Create a business
portfolio"** klicken (oder business.facebook.com → *Business Portfolio
erstellen*). Name "Selma Nuhija", Selmas E-Mail. Danach erscheint das
Portfolio oben links in business.facebook.com. Das bestehende Werbekonto
wird im nächsten Schritt hineingeholt, es geht nichts verloren.

### 1.1 Selma: Business Portfolio öffnen und drei Dinge prüfen
business.facebook.com → oben links das Portfolio auswählen → Zahnrad
*Einstellungen*. Dort nacheinander:
1. *Konten → Instagram-Konten*: Steht @selmanuhija drin? Wenn nicht:
   *Hinzufügen* → Instagram-Login. (Das Instagram-Konto muss ein
   Professional-Konto sein: Instagram-App → Profil → ☰ → *Kontotyp und Tools*.
   Steht dort "Zu einem Business-Konto wechseln", einmal wechseln.)
2. *Konten → Seiten*: Hängt ihre Facebook-Seite drin? Sie bleibt reiner
   technischer Träger, es wird nichts darauf beworben.
3. *Konten → Werbekonten* → *Hinzufügen* → **"Neues Werbekonto erstellen"**.
   Name "Selma Ads", Zeitzone Europe/Berlin, Währung EUR, Zweck "für mein
   Unternehmen". Das alte persönliche Konto 956540482250069 lässt sich nicht
   übernehmen, weil darüber nie bezahlt wurde (Meta-Fehler "Cannot move
   account"). Es bleibt ungenutzt liegen. **Erledigt 17.10.: neue ID
   act_2982640922095203.**
4. Beim Werbekonto: *Zahlungsmethode* vorhanden? Sonst Karte oder PayPal
   hinterlegen. *Geschäftsinformationen* (Adresse, ggf. USt-ID) ausgefüllt?
   Meta braucht das für Rechnungen in der EU.

### 1.2 Selma: dich hinzufügen
*Einstellungen → Personen* → *Personen hinzufügen* → deine Facebook-E-Mail →
Zugriff **"Vollständige Kontrolle"** (einfachster Weg). Du bekommst eine
Mail, nimmst an, fertig.

### 1.3 Du: Werbekonto öffnen
adsmanager.facebook.com → oben links "Selma Ads" wählen. Siehst du die
Kampagnenliste und den Button "Erstellen", ist Phase 1 fertig. Eventuell
liegen dort alte Kampagnen oder "Beitrag bewerben"-Reste: nichts löschen,
nur anschauen und mir sagen, was da ist.

**Phase 1 ist fertig, wenn:** du im Werbeanzeigenmanager Selmas Konto siehst,
eine Zahlungsmethode hinterlegt ist, Instagram und Seite im Portfolio hängen.

---

## Phase 2: Angebot und Funnel festlegen (fast fertig)

Das meiste steht schon, weil Content-Pläne, Onboarding-Mails und Website-Texte
existieren. Siehe `kunde/selma.md`. Was ich daraus übernommen habe:

- **Angebot:** Mitgliedschaft 70 €/Monat, monatlich kündbar, Einstieg jederzeit.
- **Funnel:** Der organische Weg (Reel → Keyword-Kommentar → ManyChat-DM mit
  Freebie → Flodesk-Mails → Mitgliedschaft) läuft bereits. Die Ads verstärken
  genau diesen Weg: Anzeige öffnet eine Instagram-DM, ManyChat antwortet.
  Kein Pixel, keine neue Landingpage nötig.
- **Erste Freebies für Ads:** RETTUNG und PROTEIN, beide fertig.
- **Zielgruppe und Ton:** aus den Reels-Plänen und dem Karussell-Brief.

Was du noch beantworten musst, bevor Geld fließt:

1. **ManyChat:** Ist ManyChat mit Selmas Instagram verbunden und hast du Zugang?
   Für Ads braucht ManyChat einen "Ad-Trigger" (Klick auf Anzeige startet den
   Flow), der ist im Pro-Tarif enthalten.
2. **Webseite (geklärt, siehe `kunde/webseite.md`):** eine HTML-Datei bei
   Hitrost, Impressum und Datenschutz vorhanden, kein Pixel. Zu tun:
   `website/impressum.html` und `website/datenschutz.html` ins Root bei
   Hitrost hochladen; Datenschutz-Abschnitt 12 (Meta-Werbung) von Selma
   freigeben lassen und einfügen, bevor Instant Forms laufen.
3. **Budget:** Selma bleiben 35 € pro Kundin und Monat (50 % Provision) und
   sie zahlt Werbung selbst. Deshalb klein: 10 €/Tag, vier Wochen, rund
   300 €, harte Obergrenze 10 €/Tag. Zuerst nur warme Zielgruppe. Die
   Rechnung steht in `kunde/selma.md` unter "Budget und Zielwerte".
4. **Verweildauer: 6 Monate im Schnitt (geklärt).** Damit darf eine Kundin
   70 € Werbung kosten und ein Lead etwa 7 €. Das ist machbar, aber ohne
   Luft: warme Zielgruppe zuerst, kalte nur, wenn sie unter 7 € bleibt.
5. **Hijab in Anzeigen:** geklärt, nein.
6. **Länder:** geklärt, DACH.

**Phase 2 ist fertig, wenn:** diese sechs Punkte in `kunde/selma.md` stehen und
die Werbekonto-ID aus Phase 1 eingetragen ist.

---

## Phase 3: Claude Code anbinden (du, 30 Minuten)

### 3.1 Projekt öffnen
```bash
cd Shramba/selma-ads
claude
```
Claude liest `CLAUDE.md` und kennt damit die Regeln (nichts ohne FREIGABE).

### 3.2 Meta-Ads-MCP verbinden
```bash
claude mcp add --transport http meta-ads https://mcp.facebook.com/ads
```
Dann in Claude Code `/mcp` eingeben, `meta-ads` wählen, *Authenticate*. Es
öffnet sich ein Browser mit dem Meta-Login. **Mit deinem Facebook-Login**
anmelden (nicht Selmas), im Dialog *"Opt in for current business only"* und
das Portfolio "Selma Nuhija" wählen.

In einer claude.ai-Session (wie dieser hier): Einstellungen → Connectors →
Custom Connector → URL `https://mcp.facebook.com/ads` → gleicher Login.

### 3.3 Testen, ohne etwas zu ändern
In Claude Code:
```
Liste die Werbekonten, auf die du Zugriff hast, und die Kampagnen in Selmas Konto.
```
Kommt `act_…` mit "Selma Ads" zurück, läuft die Verbindung. Kommt ein Fehler,
den Text hier in den Chat kopieren.

---

## Phase 4: Erste Kampagne (Claude, du gibst frei, Woche 1)

```
/wochenlauf
```
Claude macht beim ersten Lauf:
1. Bericht "noch keine Daten".
2. Zielgruppen-Vorschlag: eine kalte Anzeigengruppe (Frauen 35–55, DACH,
   breit) und eine warme (alle, die Selmas Reels gesehen oder ihr Profil
   besucht haben, plus die Flodesk-Liste als Kundenliste). Die warme ist bei
   7.000 Followern und vielen Reels wertvoll und günstig.
3. 3–5 Anzeigen als Text + Briefing. **Beim Start nutzen wir Selmas
   bestehende Reels als Videos**, die sind schon da und zeigen ihr Gesicht.
   Claude sagt, welche Reels zu welchem Text passen.
4. Alles pausiert im Werbekonto anlegen.
5. Zusammenfassung zur Freigabe.

Du liest die Texte, Selma liest sie auch. Dann schreibst du:
```
FREIGABE ERK-1, ALL-2, Budget 15 €/Tag
```
Erst jetzt läuft Geld.

### Was du in Woche 1 beobachtest (täglich 5 Minuten, Ads Manager oder "Zahlen?" an Claude)
- Werden Anzeigen **abgelehnt**? Dann Text zu mir, nicht selbst nachbessern.
- Gibt das Konto Geld aus? Wenn nach 24 h 0 € ausgegeben sind: Zahlungsmethode
  oder Konto-Freischaltung prüfen.
- Kommen Leads/Chats an? Selma muss **innerhalb von Stunden** antworten,
  sonst sind sie kalt.

---

## Phase 5: Wöchentlicher Rhythmus (ab Woche 2)

| Wann | Wer | Was |
|---|---|---|
| Montag | du | `/wochenlauf` in Claude Code starten, 10 Minuten lesen, FREIGABE geben |
| Montag | Selma | neue Texte lesen, ggf. ein Reel für die Woche aufnehmen (Briefing kommt von Claude) |
| Mi/Fr/So/Mo | du oder Selma | Reel des Tages auch als Short hochladen, Titel und Beschreibung aus `/youtube` |
| täglich | Selma | Leads/Chats beantworten, mir einmal pro Woche sagen, welche Leads gut waren |
| Donnerstag | du | kurz "Zahlen?" an Claude, nur eingreifen wenn etwas pausiert werden muss |
| Monatsende | du | Berichte in `berichte/` durchsehen, mit Selma Budget und Angebot besprechen |

---

## Phase 6: YouTube (parallel zu Phase 1, kein Geld nötig)

Selma will YouTube aufbauen. Das läuft unabhängig von den Ads und kostet nur
Zeit. Zwei Stufen, die zweite erst nach acht Wochen der ersten.

### 6.1 Kanal prüfen und dich eintragen (Selma, 15 Minuten)
Der Kanal existiert. Selma öffnet studio.youtube.com und prüft:
1. *Anpassung → Branding*: Profilbild wie Instagram, Banner mit ihren drei
   Sätzen (Hungern ist out. Muskeln sind in. Lifestyle ist alles.).
2. *Anpassung → Allgemeine Informationen*: Handle möglichst `@selmanuhija`,
   Kanalbeschreibung (schreibe ich), Links zu selmanuhija.com und Instagram.
3. *Einstellungen → Kanal → Erweiterte Einstellungen*: "Nein, nicht für
   Kinder".
4. *Einstellungen → Berechtigungen → Einladen*: deine Google-Adresse als
   **Bearbeiter**. So lädst du hoch und siehst die Zahlen, ohne ihr Passwort.
5. Mir den Kanal-Link schicken, dann schaue ich, was schon drauf ist und ob
   die alten Videos zur jetzigen Positionierung passen.

### 6.2 Stufe 1: Shorts aus den Reels (ab sofort, 4 pro Woche)
- Jedes neue Reel wird am selben Tag auch als Short hochgeladen. Die Datei
  ist dieselbe, aber **ohne Instagram-Wasserzeichen**: Original aus CapCut
  oder vom Handy nehmen, nicht von Instagram herunterladen.
- Das Keyword-Spiel ("Schreib RETTUNG") gibt es auf YouTube nicht. Im Video
  bleibt der Satz, in der Beschreibung und im angepinnten Kommentar steht
  stattdessen der Link zum Freebie. Dafür braucht jedes Freebie eine kleine
  Seite auf selmanuhija.com mit Flodesk-Formular (z. B. `/rettung`,
  `/protein`). Das baue ich, sobald ich an die Seite komme.
- `/youtube` liefert jede Woche Titel, Beschreibung, Hashtags und den
  angepinnten Kommentar für die vier Shorts.

### 6.3 Stufe 2: lange Videos (ab Woche 9, zwei pro Monat)
- 8–12 Minuten, eine Suchfrage pro Video, Selma spricht in die Kamera,
  dazwischen Teller- oder Küchenaufnahmen. Handy, Tageslicht, Küche.
- Themen sind die acht Alltagsprobleme aus dem Content-Plan. `/youtube`
  schreibt Skript, Titel, Beschreibung, Kapitel, Thumbnail-Text.
- Ein Drehtag pro Monat reicht für beide Videos.

### 6.4 YouTube-Ads
Erst, wenn Instagram-Ads vier Wochen gelaufen sind und aus Stufe 2 Videos
existieren, die organisch funktionieren. Läuft dann über Google Ads, mit
denselben Freigabe-Regeln.

---

## Was du mir als nächstes schickst

1. Die sechs Antworten aus Phase 2, Stichpunkte reichen.
2. Wo die Webseite liegt und ob du mir den Quellcode oder Zugang geben kannst.
   Dann prüfe ich Impressum, Datenschutz und Pixel selbst und baue bei Bedarf
   eine Seite `/start` für die Mitgliedschaft.
3. Die Werbekonto-ID `act_…`, sobald Phase 1 steht.
4. Links zu den 5 Reels mit den meisten Aufrufen. Die werden das erste
   Anzeigenmaterial.
