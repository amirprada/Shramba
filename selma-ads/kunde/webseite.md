# Webseite selmanuhija.com – Befund (Quellcode vom 18.10.2026)

Quelle: `website/index.html` (Live-Stand, von Amir geliefert). Englische und
bosnische Version liegen als `selma-website-en.html` und `selma-website-bs.html`
auf dem Server, hier nicht vorhanden.

## Technik
- **Eine HTML-Datei**, alle Unterseiten sind Abschnitte, Navigation per
  Hash-Routing (`#home`, `#coaching`, `#guide`, `#impressum`, `#datenschutz` …).
  Direktlinks funktionieren: `https://selmanuhija.com/#datenschutz`.
- **Hosting:** HITROST.COM d.o.o., Jesenice, Slowenien (EU). Upload vermutlich
  per FTP/Dateimanager im Hitrost-Kundenbereich. Zugang: Amir.
- **Kein Meta Pixel, kein Google Analytics, kein Tag Manager.** Cookie-Banner
  nur für YouTube-Einbettungen ("technisch notwendig" + "externe Videos").
- **Formulare:** Flodesk (eingebettet als `fd-form-…` für Erstgespräch und
  Guide-Modal) plus drei externe Flodesk-Links für Guides.
- **Fonts:** Cormorant Garamond + Montserrat über Google Fonts.

## Angebot und Kaufweg
- **VIP Membership: 79 $ pro Monat (ca. 70 €), monatlich kündbar.**
  4 Wochen Onboarding, danach laufende Begleitung.
- **Der Kauf passiert nicht auf selmanuhija.com**, sondern über den
  Affiliate-Link `fasterwaycoach.com/vip-membership?aid=selmanuhija`.
  Folge: Ein Pixel auf Selmas Seite kann nie einen Kauf messen. Messbar sind
  nur Seitenaufrufe, Guide-Anfragen und Erstgespräch-Anmeldungen.
- **Erstgespräch:** 15 Minuten, kostenlos, Formular (Vorname + E-Mail, Flodesk,
  Double-Opt-In). Das ist der stärkste Lead-Einstieg der Seite.
- **Kontakt:** selma.wellness@selmanuhija.com, kein WhatsApp-Link, kein Calendly.

## Freebies auf der Seite (Abschnitt `#guide`)
| Guide | Status | Link |
|---|---|---|
| 5 schnelle Familienrezepte (PDF) | live | https://fancy-wave-35324.myflodesk.com/b3qrm2i05u |
| 3 protein-reiche Frühstücke (PDF) | live | https://fancy-wave-35324.myflodesk.com/ulmzrd47su |
| Cortisolbauch in der Lebensmitte (PDF) | live | https://fancy-wave-35324.myflodesk.com/afmucnrqxi |
| 3-Tage-Plan 1.600 kcal / 120 g Protein (Flodesk-Formular, 18.10.) | live, nicht auf der Webseite verlinkt | https://fancy-wave-35324.myflodesk.com/3-tage-plan |
| 30-Minuten-Trainingsguide (Flodesk-Formular, 18.10.) | live, nicht auf der Webseite verlinkt | https://fancy-wave-35324.myflodesk.com/trainingsguide |
| Lean Protein Liste | "bald verfügbar" | – |
| Insulin Guide (11 Strategien) | "bald verfügbar" | – |
| Ballaststoff-Hebel | "bald verfügbar" | – |

Die ManyChat-Freebies (RETTUNG, TAUSCH, PROTEIN, MORGEN, 30 MINUTEN, PLAN)
sind andere PDFs als die Webseiten-Guides. Für YouTube-Beschreibungen reicht
vorerst `https://selmanuhija.com/#guide` als Sammel-Link, oder die drei
Flodesk-Links direkt.

## Rechtliches
- **Impressum vorhanden** (`#impressum`): Selma Nuhija-Keric, Zanderstraße 12,
  53177 Bonn. Kleinunternehmerin § 19 UStG, keine USt-ID. Stand Mai 2026.
- **Datenschutzerklärung vorhanden** (`#datenschutz`), 11 Abschnitte: Hosting
  Hitrost, Logfiles, Cookies, Kontakt, Flodesk + ManyChat (inkl. Instagram-
  Anforderung, DPF), YouTube, Weiterleitung FASTer Way, Rechte, Beschwerde,
  Speicherdauer. Stand Mai 2026.
- **Fehlt:** ein Abschnitt zu Meta-Werbeanzeigen und Lead-Formularen. Für den
  DM-Funnel (Variante A) ist ManyChat/Instagram bereits abgedeckt. Sobald
  **Instant Forms (Variante B)** oder ein **Pixel** kommen, muss ein Abschnitt
  "Werbung auf Instagram (Meta)" ergänzt werden. Entwurf unten.
- **Standalone-Seiten erzeugt:** `website/impressum.html` und
  `website/datenschutz.html`, 1:1 aus den Abschnitten der Live-Seite, eigener
  Kopf, `noindex`. Grund: Meta akzeptiert als Datenschutz-URL im Instant Form
  zuverlässiger eine echte Seite als einen Hash-Link. Amir lädt beide ins
  Root-Verzeichnis bei Hitrost; danach gelten
  `https://selmanuhija.com/datenschutz.html` und
  `https://selmanuhija.com/impressum.html`.

## Entwurf: Datenschutz-Abschnitt "12. Werbung auf Instagram (Meta)"
(von Selma freigeben lassen, dann in `index.html` unter Abschnitt 11 einfügen
und in `datenschutz.html` ebenso)

> **12. Werbeanzeigen auf Instagram (Meta)**
> Ich schalte Werbeanzeigen auf Instagram über Meta Platforms Ireland Ltd.,
> Merrion Road, Dublin 4, Irland. Wenn du über eine Anzeige eine Nachricht
> an mich schreibst oder ein Formular ("Instant Form") ausfüllst, übermittelt
> Meta mir die von dir eingegebenen Daten (z. B. Vorname, E-Mail-Adresse).
> Ich verwende sie ausschließlich, um dir den angeforderten Inhalt zu senden
> oder deine Anfrage zu beantworten; die weitere Verarbeitung läuft wie unter
> Punkt 6 beschrieben über Flodesk bzw. ManyChat. Rechtsgrundlage ist deine
> Einwilligung (Art. 6 Abs. 1 lit. a DSGVO), die du jederzeit per E-Mail an
> selma.wellness@selmanuhija.com widerrufen kannst. Welche Daten Meta beim
> Ausspielen von Anzeigen selbst verarbeitet, erklärt Meta in seiner
> Datenrichtlinie: https://www.facebook.com/privacy/policy. Ein Meta-Pixel
> ist auf dieser Website nicht eingebunden.
> Um meine Anzeigen gezielt auszuspielen, kann ich Meta außerdem eine
> verschlüsselte (gehashte) Liste von E-Mail-Adressen meiner Abonnentinnen
> übermitteln ("Custom Audience"). Meta nutzt sie nur zum Abgleich mit
> bestehenden Konten und löscht die Hashes nach dem Abgleich. Rechtsgrundlage
> ist mein berechtigtes Interesse an der Ansprache bestehender Kontakte
> (Art. 6 Abs. 1 lit. f DSGVO); du kannst dem jederzeit per E-Mail
> widersprechen.

## Was die Seite für Ads und YouTube liefert
- **Datenschutz-URL** für Instant Forms: `https://selmanuhija.com/datenschutz.html`
  (nach Upload), bis dahin `https://selmanuhija.com/#datenschutz`.
- **Landingpage für Kaufinteresse:** `https://selmanuhija.com/#coaching`
  (Investment-Abschnitt mit Preis) und `#erstgespraech`.
- **Freebie-Links** für YouTube: siehe Tabelle oben.
- **Pixel:** vorerst nicht einbauen. Ohne Kauf auf der eigenen Seite bringt er
  wenig, und er verlangt Cookie-Einwilligung plus Datenschutz-Update. Erst
  wenn Variante C getestet wird.

## Kleine Punkte für später (nicht dringend)
- Preis steht in Dollar ("79 $ pro Monat, ca. 70 €"). In Anzeigen nur
  "ca. 70 € im Monat" oder gar kein Preis.
- `og:image` prüfen (Vorschaubild beim Teilen des Links in DMs).
- Drei Guides stehen auf "bald verfügbar". Jeder davon wäre ein neues
  Keyword für Reels und Shorts.
