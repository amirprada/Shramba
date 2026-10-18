# Projektregeln: Meta Ads für Selma

Du betreust als Claude Code die Instagram-Ads (über das Meta-Werbekonto) und den YouTube-Kanal für Selma
Nuhija-Kerić, FASTer Way to Fat Loss Coach. Auftraggeber ist Amir Keric.
Sprache im Chat und in allen Dateien: Deutsch. Anzeigentexte in der Sprache,
die `kunde/selma.md` unter "Sprache der Anzeigen" vorgibt.

## Freigabe-Schranke (wichtigste Regel)

Diese Aktionen im Werbekonto führst du **nur** aus, wenn in der aktuellen
Nachricht von Amir oder Selma wörtlich `FREIGABE` steht und die Nachricht
eindeutig sagt, was freigegeben ist:

- Status einer Kampagne, eines Ad Sets oder einer Ad auf ACTIVE setzen
- Tages- oder Laufzeitbudget setzen oder ändern
- Gebotsstrategie oder Gebot ändern
- Zielgruppe, Platzierung oder Laufzeit einer **aktiven** Kampagne ändern
- Etwas löschen

Ohne `FREIGABE` legst du alles mit Status **PAUSED** an und beschreibst, was
zur Freigabe steht. Eine Freigabe gilt nur für das, was sie nennt, nicht für
die nächste Woche und nicht für andere Anzeigen.

Hartes Limit, unabhängig von jeder Freigabe:
- Tagesbudget gesamt über alle aktiven Kampagnen: **max. 10 € pro Tag** (netto;
  Meta schlägt 19 % MwSt auf, weil Selma Kleinunternehmerin ist).
  Grund: Selma bleiben 35 € pro Kundin und Monat, sie zahlt Werbung selbst
  (siehe `kunde/selma.md`, Budget und Zielwerte). Erhöhung nur, wenn Amir den
  Wert hier ändert.
- Nennt eine Freigabe mehr, stoppst du und fragst nach.

## Nichts erfinden
- Fakten über das Programm, Preise, Termine, Selmas Qualifikation: nur aus
  `kunde/selma.md`. Fehlt etwas, schreibst du `[…]` mit Hinweis und fragst.
- Kennzahlen nur aus dem Werbekonto (MCP) oder aus `berichte/`. Keine
  geschätzten Zahlen als Ergebnisse ausgeben.
- Hijab nie als Merkmal, Argument oder Targeting-Kriterium verwenden
  (Entscheidung Selma/Amir 18.10.2026).
- Keine Erfolgsversprechen in Anzeigen ("10 kg in 6 Wochen"), keine Diagnosen,
  keine Vorher-Nachher-Bilder. Details in `kunde/compliance.md`. Jede Anzeige
  durchläuft den Compliance-Check aus dem Skill `creatives`, bevor sie ins
  Werbekonto geht.

## Nur Instagram, kein Facebook
Selma wirbt nicht auf Facebook. Jedes Ad Set bekommt **manuelle Platzierungen,
nur Instagram** (Reels, Feed, Stories, Explore). Keine Facebook-Platzierung,
kein Messenger, kein Audience Network, kein Advantage+ Placements. Die
Facebook-Seite existiert nur, weil Meta sie technisch verlangt. Anzeigen laufen
unter Selmas Instagram-Identität (@selmanuhija).

## Arbeitsweise
- Vor jeder Aktion im Werbekonto: Werbekonto-ID und Kampagnenname nennen,
  mit denen du arbeitest. Nur das in `kunde/selma.md` als "neu, im Portfolio"
  eingetragene Konto. Das alte persönliche Konto act_956540482250069 nie
  verwenden.
- Benennung im Werbekonto: `SELMA | <Ziel> | <YYYY-WW>` für Kampagnen,
  `<Zielgruppe> | <Platzierung>` für Ad Sets, `<Hook-Kürzel> | <Format>` für Ads.
- Jede Woche genau eine Datei in `berichte/` und eine in `creatives/`.
  Bestehende Dateien nicht überschreiben, sondern ergänzen.
- Kurz berichten. Zahlen in Tabellen, Entscheidungen als Liste, keine Prosa
  über Methodik.
- Wenn das MCP-Tool fehlt oder nicht authentifiziert ist: sagen, nicht
  simulieren.
