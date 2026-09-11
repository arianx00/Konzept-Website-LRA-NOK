import os
import re

files_to_patch = ["service.html", "service-alle.html"]

def replacer(match):
    url = match.group(1)
    text = match.group(2)
    # KFZ-Zulassung hat eine echte Seite, daher nicht ersetzen
    if "service-kfz.html" in url or "KFZ-Zulassung" in text:
        return f'<li><a href="service-kfz.html">{text}</a></li>'
    return f'<li><a href="dummy-formular.html">{text}</a></li>'

for filename in files_to_patch:
    filepath = os.path.join(r"C:\Users\Arian\Desktop\Website LRA", filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Ersetzt alle direkten Links innerhalb von <li> (die Kachel-Unterpunkte)
    patched_content = re.sub(r'<li><a href="([^"]+)">(.*?)</a></li>', replacer, content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(patched_content)

print("Kachel-Links erfolgreich auf dummy-formular.html umgeleitet!")
