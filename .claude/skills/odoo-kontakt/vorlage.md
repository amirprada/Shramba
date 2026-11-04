# Eingabe-Vorlage für odoo-kontakt

Kopfzeilen der Datei:
```
status: offen            (offen | teilweise | eingepflegt)
anlass: <Messe/Besuch/Call – Ort>
datum: <YYYY-MM-DD>
```

Pro Person ein Block. Unsichere Lesarten mit `[?]`, Unleserliches mit `[unleserlich]`.

```
## <Vorname Nachname>
- Firma/Institut: 
- Abteilung/Standort: 
- Position: 
- E-Mail: 
- Telefon: 
- Sprache: 
- Anlass/Datum: 
- Gesprächsnotiz:
  - 
- Nächster Schritt (Aktivität): <Typ: E-Mail|Anruf|Besprechung|Zu erledigen> – <Zusammenfassung> – fällig <Datum|+7 Tage>
- Weitere Personen im Gespräch: 
- Unsicherheiten: 
```

Am Ende der Datei: `## Offene Fragen an Amir` (nummeriert) und nach Phase 2 `## Bericht <Datum>`.
