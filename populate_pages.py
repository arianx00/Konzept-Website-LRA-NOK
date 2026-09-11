import os
import json

data = {
    "service-auto.html": {
        "title": "Auto, KFZ & Führerschein",
        "sections": {
            "Zulassung": [
                "Online-KFZ-Zulassung",
                "Wunschkennzeichen"
            ],
            "Führerschein": [
                "Digitaler Führerscheinantrag (Online)",
                "Umtausch bzw. Umstellung Führerschein in EU-Kartenführerschein",
                "Ersterteilung/Erweiterung/Verlängerung einer Fahrerlaubnis/Begleitetes Fahren ab 17",
                "Umschreibung einer ausländischen Fahrerlaubnis",
                "Internationaler Führerschein",
                "Fahrerqualifikationsnachweis (FQN)",
                "Antrag auf Erteilung einer Fahrlehrerlaubnis",
                "Antrag auf Erteilung einer Fahrschulerlaubnis",
                "Ausnahmegenehmigung nach § 70 Straßenverkehrs-Zulassungs-Ordnung (StVZO)"
            ]
        }
    },
    "service-einwanderung.html": {
        "title": "Einwanderung, Aufenthalt & Asyl",
        "sections": {
            "Spätaussiedler": ["Opferpension"],
            "Leistungen für Asylbewerber & Unterbringung": [
                "Antrag auf Leistungen für Bildung und Teilhabe",
                "Hinweise zum Ausfüllen des Antrags auf Leistungen für Bildung und Teilhabe",
                "Mietbescheinigung Wohnung AsylbLG",
                "Antrag auf Gewährung von Leistungen nach dem Asylbewerberleistungsgesetz (AsylbLG)"
            ],
            "Ausländerangelegenheiten & Aufenthalt": [
                "Antrag auf Änderung der Wohnsitzauflage Asyl",
                "Online-Anträge der Ausländerbehörde (wichtig!)",
                "Verpflichtungserklärung - „Abgabe oder Vorbereitung einer Verpflichtungserklärung“"
            ],
            "Einbürgerung": [
                "Einwilligungserklärung zum Einbürgerungsantrag",
                "Antrag auf Einbürgerung in der Bundesrepublik Deutschland nach dem Staatsangehörigkeitsgesetz (StAG)",
                "Bescheinigung mietfreies Wohnen",
                "5-Bekenntnis Loyalitätserklärung neu Felder",
                "8-Erklärung zum Einbürgerungsantrag Felder"
            ]
        }
    },
    "service-soziales.html": {
        "title": "Soziales, Jugend, Senioren & Familie",
        "sections": {
            "Beistandschaft": [
                "Antrag auf Ausstellung einer Negativbescheinigung",
                "Antrag Beistandschaft",
                "Erklärung zur Beendigung der Beistandschaft"
            ],
            "Bildungs- & Teilhabepaket": [
                "Antrag Bildung und Teilhabe - Stand 08 2024",
                "Vordruck Ausflug-Klassenfahrt"
            ],
            "Grundsicherung im Alter und bei Erwerbsminderung": [
                "Antrag Grundsicherung und HLU - 13.07.2023",
                "Mietbescheinigung - Antrag - 23.10.2019"
            ],
            "Hilfe zur Überwindung sozialer Schwierigkeiten": [
                "Antrag auf Leistungen zum Erhalt der Wohnung bei Inhaftierung - Antrag - 02.03.2022"
            ],
            "Entschädigungsrecht & Opferpension": [
                "Antrag auf Gewährung von Beschädigtenversorgung (BVG)",
                "Antrag auf Gewährung von Beschädigtenversorgung (OEG)",
                "Antrag auf Gewährung von Beschädigtenversorgung (ZDG)",
                "Antrag auf Gewährung von Beschädigtenversorgung (IfSG)",
                "Antrag auf Gewährung von Hinterbliebenenversorgung (BVG)",
                "Antrag auf Gewährung von Hinterbliebenenversorgung (OEG)",
                "Antrag auf Gewährung von Versorgung nach StrRehaG",
                "Antrag auf Gewährung von Versorgung nach VwRehaG",
                "Antrag auf Rentenkapitalisierung"
            ]
        }
    },
    "service-sicherheit.html": {
        "title": "Sicherheit & Ordnung",
        "sections": {
            "Personenstand & Name": [
                "Antrag Vornamensänderung",
                "Antrag Änderung - Feststellung Familiennamen"
            ],
            "Ordnungs- & Polizeibehörde": [
                "Anmeldung einer Versammlung unter freiem Himmel gemäß § 14 Versammlungsgesetz",
                "Antrag auf Zulassung zur Verhaltensprüfung nach § 1 Absatz 4 Polizeiverordnung über das Halten gefährlicher Hunde",
                "Erhebungsbogen zur Verhaltensprüfung nach § 1 Absatz 4 der Polizeiverordnung über das Halten gefährlicher Hunde"
            ],
            "Waffen & Munition": [
                "Antrag Mitnutzerlaubnis",
                "Anzeige Deaktivierte Waffen",
                "Anzeige erlaubnispflichtige Schusswaffen",
                "Anzeige von Magazinen gem. § 58 Absatz 17 WaffG"
            ]
        }
    },
    "service-tiere.html": {
        "title": "Tiere, Landwirtschaft & Lebensmittel",
        "sections": {
            "Lebensmittel- & Fleischhygiene": [
                "Bescheinigung kundige Person",
                "Registrierformular Jäger 2020",
                "Registrierung Lebensmittelunternehmer",
                "Standarderklärung-Information zur Lebensmittelkette"
            ],
            "Tiergesundheit & Tierhaltung": [
                "20240730_ASP Allgemeinverfügung NOK",
                "Tierhalterantrag zur Registrierung von Landtieren (inkl. Bienen)",
                "Tierhalterantrag zur Registrierung von Wassertieren",
                "Traces_Anmeldung Verbringen von Tieren.01-22",
                "Tierhalterantrag zur Registrierung von Landtieren (ohne Bienen)"
            ],
            "Tierschutz": [
                "Antrag auf Befähigungsnachweis zum Tiertransport nach VO 1_2005",
                "Antrag auf Erlaubnis nach § 11 Tierschutzgesetz_Handel mit Wirbeltieren",
                "Antrag auf Erlaubnis nach § 11 Tierschutzgesetz_Hundeausbildung",
                "Antrag auf Erlaubnis nach § 11 Tierschutzgesetz_Reit-Fahrbetrieb",
                "Antrag auf Erlaubnis nach § 11 Tierschutzgesetz_Zucht und Halten von Wirbeltieren",
                "Antrag Sachkundenachweis Ferkelkastration",
                "Antrag Sachkundenachweise Gatterwild (VO 1099_2009)",
                "Antrag Sachkundenachweise Schlachten (VO 1099_2009)",
                "Antrag Transportunternehmen nach VO 1_2005",
                "Anzeige Zirkusgastspiel (§16(1a) TierSchG)"
            ]
        }
    },
    "service-abfall.html": {
        "title": "Abfall & Entsorgung",
        "sections": {
            "Abfallrecht": [
                "Antrag auf Erlaubnis nach § 54 KrWG",
                "Anzeige von Sammlern, Beförderern, Händlern und Maklern von Abfällen nach § 53 Kreislaufwirtschaftsgesetz",
                "Anzeige gemeinnützige Sammlung",
                "Anzeige gewerbliche Sammlung",
                "GewAbfVO – Dokumentation Bau- und Abbruchabfälle",
                "GewAbfVO – Dokumentation gewerbliche Siedlungsabfälle"
            ]
        }
    },
    "service-bauen.html": {
        "title": "Bauen, Wohnen & Immobilien",
        "sections": {
            "Bauen & Wohnen": [
                "ViBA-BW (Virtuelles Bauamt Baden-Württemberg)",
                "Kimberly"
            ]
        }
    },
    "service-umwelt.html": {
        "title": "Umwelt, Wasser & Naturschutz",
        "sections": {
            "Immissionsschutz": [
                "Änderung einer genehmigungsbedürftige Anlage anzeigen",
                "Unterlagen für Immissionsschutzrechtliche Genehmigung nachreichen",
                "Genehmigung nach dem Bundes-Immissionsschutzgesetz beantragen"
            ],
            "Wasserrecht, Bodenschutz & Altlasten": [
                "Onlineantrag zum Entnehmen und Ableiten von Wasser aus oberirdischen Gewässern",
                "Formulare zur Neu- und Ummeldung von Anlagen an die Wasserbehörden nach der AwSV",
                "Liste der anerkannten Sachverständigen nach der AwSV",
                "Infos und Broschüren zum Hochwasserschutz und zum Bauen in Überschwemmungsgebieten",
                "Wasserentnahmeentgelt - Erklärung zur Festsetzung",
                "Vordruck für Neuerteilung EWS 01-2024",
                "Tabelle-Heizöltanks-Prüfzeitpunkte -AwSV-2025"
            ],
            "Naturschutz": [
                "Natura 2000-Vorprüfung-Formblatt NOK Stand 05-2009",
                "201019 NOK-Formblatt zur Beantragung einer Ausnahme nach § 21 Absatz 5 NatSchG"
            ],
            "Gewässer, Boden & Altlasten": [
                "Wasserentnahme erklären",
                "Entnehmen, Ableiten von Wasser aus oberirdischen Gewässern beantragen",
                "Jauche-Gülle-Silagesickersaft-Anlage anzeigen",
                "Betreiberwechsel anzeigen",
                "Heizölverbraucheranlage anzeigen",
                "Allgemeine Anzeige (außer Heizöl- und JGS-Anlagen)",
                "Benutzung eines Gewässers - Erlaubnis zum Entnehmen, Zutagefördern, Zutageleiten und Ableiten von Grundwasser beantragen",
                "Antragsformular Gartenbrunnen"
            ]
        }
    },
    "service-unternehmen.html": {
        "title": "Unternehmen, Gewerbe & Arbeitsschutz",
        "sections": {
            "Arbeitsschutz & Gewerbeaufsicht": [
                "Formulare zur Vorankündigung einer Baustelle",
                "Formulare zu Gefahrstoffen (Anzeige zum Umgang mit Asbest und Begasungsmittlen)",
                "Formulare zum Arbeitszeitrecht (Antrag auf Bewilligung von Sonn- und Feiertagsarbeit)",
                "Jugendarbeitsschutz – Informationen und Formulare",
                "Formulare und Informationen zu 44.BlmSchV",
                "Antrag auf Bewilligung der Beschäftigung von Arbeitnehmer(inne)n an bis zu 5 Sonn- bzw. Feiertagen im Jahr nach § 13 Abs. 3 Nr. 2 Buchst. b Arbeitszeitgesetz"
            ],
            "Gewerbeangelegenheiten": [
                "Antrag auf Erteilung, Verlängerung, Ausdehnung einer Reisegewerbekarte",
                "Antrag auf Erteilung einer Erlaubnis zum Betrieb einer Spielhalle nach § 41 Landesglücksspielgesetz",
                "Antrag Festsetzung einer Veranstaltung (Messe, Ausstellung, Markt) nach §60, §64, §65, §66, §67 oder §68 Gewerbeordnung",
                "Antrag auf Erteilung einer Konzession zum Betrieb einer Privatkrankenanstalt gemäß § 30 Gewerbeordnung",
                "Antrag auf Erteilung einer Erlaubnis zum Betrieb eines Bewachungsgewerbes nach § 34a Gewerbeordnung"
            ]
        }
    }
}

template = """<!DOCTYPE html>
<html lang="de" dir="ltr">
<head>
<meta charset="UTF-8">
<title>{title} | Digitales Landratsamt NOK</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@kern-ux/native@2.7.2/dist/kern.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@kern-ux/native@2.7.2/dist/fonts/fira-sans.css">
<style>
    :root {{ --nok-gruen: #94c11f; --nok-blau: #1a7b9b; }}
    body {{ font-family: 'Fira Sans', sans-serif; background: #f4f7f6; margin:0; color: #303030; }}
    .ds-top-bar {{ background: #fff; padding: 12px 24px; border-bottom: 1px solid #eaeaea; display: flex; align-items: center; justify-content: space-between; }}
    .ds-top-bar a.back-link {{ font-weight: 600; display: inline-flex; align-items: center; gap: 8px; font-size: 1rem; color: #555; text-decoration: none; }}
    .ds-top-bar a.back-link:hover {{ color: var(--nok-blau); }}
    .content {{ max-width: 1000px; margin: 40px auto; padding: 40px; background: #fff; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }}
    h1 {{ color: var(--nok-blau); margin-top: 0; font-size: 2.2rem; }}
    
    .section-block {{ margin-top: 50px; }}
    .section-block h2 {{ font-size: 1.4rem; color: #303030; padding-bottom: 10px; border-bottom: 2px solid #f0f0f0; margin-bottom: 20px; }}
    .form-list {{ list-style: none; padding: 0; margin: 0; }}
    .form-list li {{ margin-bottom: 12px; }}
    .form-list li a {{ display: flex; align-items: flex-start; gap: 12px; padding: 16px; background: #fafafa; border: 1px solid #eee; border-radius: 6px; text-decoration: none; color: #444; transition: border-color 0.2s, background 0.2s; font-weight: 500; line-height: 1.4; }}
    .form-list li a:hover {{ border-color: var(--nok-blau); background: #f0f8fb; color: var(--nok-blau); }}
    .form-list li a svg {{ flex-shrink: 0; color: var(--nok-gruen); margin-top: 2px; }}
</style>
</head>
<body>
    <header class="ds-top-bar">
        <a href="service-alle.html" class="back-link">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
            Zurück zur Übersicht
        </a>
        <img src="logo-nok.png" height="35" style="filter: drop-shadow(0 1px 2px rgba(0,0,0,0.1));" alt="Logo">
    </header>
    <div class="content">
        <h1>{title}</h1>
        <p style="font-size: 1.1rem; color: #555;">Wählen Sie das passende Formular oder die Online-Dienstleistung aus.</p>
        
        {sections_html}
    </div>
</body>
</html>"""

svg_icon = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>'

for filename, info in data.items():
    sections_html = ""
    for sec_name, forms in info["sections"].items():
        sections_html += f"<div class='section-block'>\n<h2>{sec_name}</h2>\n<ul class='form-list'>\n"
        for form in forms:
            href = "service-kfz.html" if "KFZ-Zulassung" in form else "dummy-formular.html"
            sections_html += f"<li><a href='{href}'>{svg_icon} <span>{form}</span></a></li>\n"
        sections_html += "</ul>\n</div>\n"
    
    filepath = os.path.join(r"C:\Users\Arian\Desktop\Website LRA", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(template.format(title=info["title"], sections_html=sections_html))

print("Alle Detailseiten erfolgreich befüllt!")
