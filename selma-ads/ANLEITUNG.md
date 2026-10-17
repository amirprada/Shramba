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

## Phase 1: Zugänge und Konten (Selma + du, ca. 1–2 Stunden)

Ziel: Du kannst in Selmas Werbekonto arbeiten, ohne ihr Passwort zu haben.

### 1.1 Selma: Instagram auf Professional-Konto prüfen
Instagram-App → Profil → ☰ → *Einstellungen und Privatsphäre* → *Kontotyp
und Tools*. Steht dort "Zu einem Business-Konto wechseln", ist sie noch
privat → wechseln (Creator oder Business, beides geht). Das verifizierte
Häkchen bleibt.

### 1.2 Selma: Facebook-Seite haben oder anlegen (nur technisch)
Selma wirbt nicht auf Facebook, und das bleibt so. Meta verlangt trotzdem
eine Facebook-Seite als Träger des Werbekontos, auch wenn jede Anzeige nur
auf Instagram läuft. Auf facebook.com → Menü → *Seiten* → *Neue Seite
erstellen*. Name "Selma Nuhija – Ernährung, Kraft, Fettabbau", Kategorie
"Coach". Profilbild wie auf Instagram. Keine Posts nötig, niemand muss sie
finden. Im Werbekonto stellt Claude jede Anzeigengruppe auf "manuelle
Platzierungen, nur Instagram".

### 1.3 Selma: Business Portfolio anlegen
business.facebook.com → *Business Portfolio erstellen* → Name "Selma Nuhija",
ihre E-Mail. Dann unter *Einstellungen* (Zahnrad, unten links):
1. *Konten → Seiten* → *Hinzufügen* → ihre Facebook-Seite.
2. *Konten → Instagram-Konten* → *Hinzufügen* → @selmanuhija (sie loggt
   sich einmal ein).
3. *Konten → Werbekonten* → *Hinzufügen* → *Neues Werbekonto erstellen*.
   Name "Selma Ads", Zeitzone Europe/Berlin, Währung EUR. Die ID `act_…`
   notieren und in `kunde/selma.md` eintragen.
4. *Zahlungsmethode* beim Werbekonto hinterlegen (Kreditkarte oder PayPal).
   Ohne das läuft nichts.
5. *Geschäftsinformationen* ausfüllen: Adresse, Steuer-/USt-ID falls
   vorhanden. Meta verlangt das für Rechnungen in der EU.

### 1.4 Selma: dich hinzufügen
Im Business Portfolio → *Einstellungen → Personen* → *Personen hinzufügen* →
deine E-Mail (die, mit der du bei Facebook bist). Zugriffsstufe
**"Vollständige Kontrolle"** (einfacher) oder "Teilweiser Zugriff" mit
Häkchen bei Seite "Inhalte verwalten", Instagram "Inhalte verwalten",
Werbekonto "Kampagnen verwalten" + "Performance anzeigen".
Du bekommst eine E-Mail, nimmst an, fertig.

Alternative für später, wenn du mehrere Kundinnen betreust: eigenes
Business Portfolio auf deinen Namen und dich als **Partner** eintragen
lassen. Für den Start nicht nötig.

### 1.5 Du: Werbekonto öffnen
adsmanager.facebook.com → oben links das Konto "Selma Ads" auswählen.
Siehst du eine leere Kampagnenliste und kannst "Erstellen" klicken, ist
Phase 1 fertig.

**Phase 1 ist fertig, wenn:** du im Werbeanzeigenmanager Selmas Konto siehst,
eine Zahlungsmethode hinterlegt ist, Seite und Instagram im Portfolio hängen.

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
2. **Webseite:** Wo liegt selmanuhija.com (Wix, Squarespace, Framer, WordPress,
   Netlify, eigener Server)? Gibt es Impressum und Datenschutzerklärung als
   eigene Seiten mit URL? Ist ein Meta Pixel eingebaut? Das brauche ich für
   Instant Forms (Datenschutz-URL) und später für Variante C.
3. **Budget:** Testbudget pro Tag und harte Obergrenze. Vorschlag 15 €/Tag,
   Obergrenze 20 €, vier Wochen. Das sind rund 450 € Lehrgeld, die man einplanen
   muss.
4. **Was darf eine Kundin kosten?** Bei 70 €/Monat hängt das davon ab, wie lange
   Kundinnen im Schnitt bleiben. Selma weiß das grob. Drei Monate wären 210 €
   Umsatz, dann sind 50 bis 70 € Werbekosten pro Kundin vertretbar.
5. **Hijab in Anzeigen** bewusst als Merkmal nutzen oder nicht? Selma entscheidet.
6. **Länder:** nur Deutschland, oder DACH?

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

### 6.1 Kanal einrichten (Selma, 30 Minuten)
1. Google-Konto von Selma → youtube.com → Profilbild → *Kanal erstellen*.
   Name "Selma Nuhija", Handle `@selmanuhija` (wenn frei).
2. Kanalbild = Instagram-Profilbild, Banner mit ihren drei Sätzen
   (Hungern ist out. Muskeln sind in. Lifestyle ist alles.). Kanalbeschreibung
   schreibe ich.
3. Link zu selmanuhija.com und Instagram im Kanal hinterlegen.
4. Unter *Einstellungen → Kanal → Erweiterte Einstellungen*: Zielgruppe
   "nicht für Kinder".
5. Amir als Kanalverwalter: YouTube Studio → *Einstellungen → Berechtigungen*
   → deine Google-Adresse als "Bearbeiter". So lädst du hoch, ohne Selmas
   Passwort.

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
