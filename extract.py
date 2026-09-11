import re

source_path = r'C:\Users\Arian\.gemini\antigravity\brain\d5a8e049-bc34-4605-a8ad-d15e61875195\.system_generated\steps\10\content.md'
html = open(source_path, encoding='utf-8').read()

start_idx = html.find('<!DOCTYPE HTML>')
if start_idx == -1:
    start_idx = html.find('<html')

html_content = html[start_idx:]

# fix absolute paths
html_content = html_content.replace('href=\"/', 'href=\"https://www.neckar-odenwald-kreis.de/')
html_content = html_content.replace('src=\"/', 'src=\"https://www.neckar-odenwald-kreis.de/')
html_content = html_content.replace('href=\'/', 'href=\'https://www.neckar-odenwald-kreis.de/')
html_content = html_content.replace('src=\'/', 'src=\'https://www.neckar-odenwald-kreis.de/')

# fix action attributes in forms
html_content = html_content.replace('action=\"/', 'action=\"https://www.neckar-odenwald-kreis.de/')

# attempt to remove the background image (which might be the nok-signet_direkt_zu.png or a body background style)
html_content = re.sub(r'background-image:\s*url\([^)]+\);?', '', html_content)
# there is an <image ... nok-signet_direkt_zu.png ...> inside the SVG, we can remove it or keep it. The user said "Bild im Hintergrund". The site has a big background image typically.

with open('index_official.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
