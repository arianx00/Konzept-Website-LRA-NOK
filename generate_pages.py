import os

pages = [
    ("service-auto.html", "Auto, KFZ & Führerschein"),
    ("service-einwanderung.html", "Einwanderung, Aufenthalt & Asyl"),
    ("service-soziales.html", "Soziales, Jugend, Senioren & Familie"),
    ("service-sicherheit.html", "Sicherheit und Ordnung"),
    ("service-tiere.html", "Tiere, Landwirtschaft & Lebensmittel"),
    ("service-abfall.html", "Abfall & Entsorgung"),
    ("service-bauen.html", "Bauen, Wohnen & Immobilien"),
    ("service-umwelt.html", "Umwelt, Wasser & Naturschutz"),
    ("service-unternehmen.html", "Unternehmen, Gewerbe & Arbeitsschutz")
]

template = """<!DOCTYPE html>
<html lang="de" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Digitales Landratsamt NOK</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@kern-ux/native@2.7.2/dist/kern.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@kern-ux/native@2.7.2/dist/fonts/fira-sans.css">
<style>
    body {{ font-family: 'Fira Sans', sans-serif; background: #f4f7f6; margin:0; color: #303030; }}
    .header {{ background: #fff; padding: 24px; border-bottom: 3px solid #1a7b9b; display: flex; align-items: center; justify-content: space-between; }}
    .content {{ max-width: 1000px; margin: 40px auto; padding: 40px; background: #fff; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }}
    h1 {{ color: #1a7b9b; margin-top: 0; }}
    .placeholder {{ margin-top: 40px; padding: 40px; border: 2px dashed #ccc; border-radius: 8px; text-align: center; color: #888; background: #fafafa; }}
    a.back-link {{ color: #1a7b9b; text-decoration: none; font-weight: bold; display: flex; align-items: center; gap: 8px; }}
    a.back-link:hover {{ text-decoration: underline; }}
</style>
</head>
<body>
    <div class="header">
        <div><a href="service.html" class="back-link">← Zurück zur Übersicht (Lebenslagen)</a></div>
        <img src="logo-nok.png" height="40" style="filter: drop-shadow(0 0 2px rgba(0,0,0,0.1));" alt="Logo">
    </div>
    <div class="content">
        <h1>{title}</h1>
        <p style="font-size: 1.1rem; color: #555;">Hier finden Sie künftig alle gebündelten digitalen Formulare, Ansprechpartner und Prozesse für diese Lebenslage.</p>
        
        <div class="placeholder">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ccc" stroke-width="2" style="margin-bottom: 16px;">
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                <line x1="9" y1="9" x2="15" y2="9"></line>
                <line x1="9" y1="13" x2="15" y2="13"></line>
                <line x1="9" y1="17" x2="15" y2="17"></line>
            </svg>
            <h3>Formulare in Vorbereitung</h3>
            <p>Die spezifischen Leistungen (z.B. Online-Anträge, PDFs und Informationsseiten) werden in den nächsten Schritten hier integriert.</p>
        </div>
    </div>
</body>
</html>"""

for filename, title in pages:
    filepath = os.path.join(r"C:\Users\Arian\Desktop\Website LRA", filename)
    # Nur überschreiben, wenn es nicht service-kfz.html ist (da wir die schon detailliert gebaut haben)
    if not os.path.exists(filepath) or filename != "service-kfz.html":
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(template.format(title=title))

print("Alle Kategorie-Seiten wurden erfolgreich erstellt!")
