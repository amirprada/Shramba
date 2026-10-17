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
| **Facebook-Seite** | Die "Firmenseite" auf Facebook. Ohne Seite keine Anzeige, auch nicht auf Instagram. | Hat sie eine? Prüfen. |
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

### 1.2 Selma: Facebook-Seite haben oder anlegen
Auf facebook.com → Menü → *Seiten* → *Neue Seite erstellen*. Name
"Selma Nuhija – Ernährung, Kraft, Fettabbau", Kategorie "Coach" oder
"Gesundheit/Wellness". Profilbild wie auf Instagram. Mehr muss auf der Seite
nicht passieren, sie ist technisch nötig.

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

## Phase 2: Angebot und Funnel festlegen (du + Selma, ein Gespräch)

Hier scheitern die meisten Werbeanzeigen, nicht an der Technik. Bevor ein
Euro fließt, müssen diese Fragen beantwortet in `kunde/selma.md` stehen:

1. **Was genau wird verkauft?** Das 6-Wochen-Programm? Ein 1:1-Coaching?
   Eine Mitgliedschaft? Zu welchem Preis? Wann startet die nächste Runde?
2. **Was passiert, wenn eine Frau Interesse hat?** Drei Wege, einen wählen:
   - **A – Instant Form:** Sie trägt Name + E-Mail/Telefon in der Anzeige
     ein, Selma ruft an oder schreibt per WhatsApp. Schnellster Start, kein
     Pixel. Nachteil: Leads sind teils unverbindlich.
   - **B – WhatsApp/Instagram-DM:** Klick auf die Anzeige öffnet einen Chat
     mit Selma. Passt perfekt zu Coaching, kostet Selma Zeit pro Chat.
   - **C – Webseite:** Klick führt auf selmanuhija.com, dort Anmeldung oder
     Terminbuchung. Braucht Pixel + funktionierende Seite. Erst wenn du mir
     die Seite gezeigt hast.
   Empfehlung für den Start: **B**, weil Selma den Kontakt persönlich macht
   und das ihr Stil ist. A als zweite Variante parallel testen.
3. **Gibt es ein kostenloses Erstangebot?** Z. B. "Protein-Guide für Frauen
   40+", "5-Tage-Challenge". Senkt die Hürde deutlich. Wenn nicht: erstmal
   ohne, später bauen.
4. **Wer ist die Frau, die kaufen soll?** Selma weiß das aus ihren Chats.
   Alter, Situation, was sie schon probiert hat, was sie nervt. Drei Sätze
   reichen, ich mache daraus die Zielgruppe.
5. **Was darf eine Kundin kosten?** Faustregel: Kostet das Programm 300 €,
   ist ein Lead für 10–25 € und eine Kundin für 100–150 € akzeptabel. Ohne
   Erfahrungswert: zwei Wochen messen, dann festlegen.
6. **Budget für den Test:** 10–20 € pro Tag für 2–4 Wochen, also 300–600 €
   Lehrgeld, das man einplanen muss. Darunter lernt man nichts.
7. **Impressum und Datenschutz:** Hat selmanuhija.com beides? Meta verlangt
   für Instant Forms eine Datenschutz-URL. Ohne geht Variante A nicht.

**Phase 2 ist fertig, wenn:** in `kunde/selma.md` keine `[…]` mehr bei
Angebot, Preis, Funnel, Link, Werbekonto-ID, Budget stehen.

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
   besucht haben). Die warme ist bei 7.000 Followern und vielen Reels
   wertvoll und günstig.
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
| täglich | Selma | Leads/Chats beantworten, mir einmal pro Woche sagen, welche Leads gut waren |
| Donnerstag | du | kurz "Zahlen?" an Claude, nur eingreifen wenn etwas pausiert werden muss |
| Monatsende | du | Berichte in `berichte/` durchsehen, mit Selma Budget und Angebot besprechen |

---

## Was du mir als nächstes schickst

1. Screenshots von selmanuhija.com (Startseite, Angebot/Preise, Impressum,
   Datenschutz), weil ich die Seite nicht aufrufen kann.
2. Antworten auf die 7 Fragen aus Phase 2, gern als Sprachnachricht
   abgetippt oder Stichpunkte.
3. Die Werbekonto-ID `act_…`, sobald Phase 1 steht.
4. Links zu 5 Reels, die Selma am besten findet. Die werden das erste
   Anzeigenmaterial.
