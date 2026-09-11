import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

css_replacement = '''
        /* SOCIAL MEDIA SECTION */
        .social-media-container {
            max-width: 1200px;
            margin: 40px auto 0;
            padding: 0 20px;
            position: relative;
        }
        .social-grid-wrapper {
            position: relative;
            margin-top: 20px;
        }
        .social-grid {
            display: flex;
            gap: 20px;
            overflow-x: auto;
            padding-bottom: 20px;
            scroll-snap-type: x mandatory;
            scrollbar-width: thin;
            scrollbar-color: var(--nok-blue) #eee;
        }
        .social-grid::-webkit-scrollbar {
            height: 8px;
        }
        .social-grid::-webkit-scrollbar-track {
            background: #eee;
            border-radius: 4px;
        }
        .social-grid::-webkit-scrollbar-thumb {
            background: var(--nok-blue);
            border-radius: 4px;
        }
        .social-card {
            flex: 0 0 280px;
            scroll-snap-align: start;
            background: #fff;
            border: 1px solid #ddd;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            display: flex;
            flex-direction: column;
            position: relative;
        }
        .social-card-img {
            width: 100%;
            height: 180px;
            object-fit: cover;
            background: #eee;
        }
        .social-card-icon {
            position: absolute;
            top: 10px;
            right: 10px;
            color: #fff;
            font-size: 22px;
            filter: drop-shadow(0 2px 4px rgba(0,0,0,0.5));
        }
        .social-card-content {
            padding: 15px;
        }
        .social-card-title {
            font-size: 14px;
            font-weight: bold;
            color: var(--text-dark);
            margin-bottom: 10px;
            line-height: 1.4;
        }
        .social-card-text {
            font-size: 12px;
            color: #666;
            line-height: 1.4;
        }
'''

content = re.sub(r'/\* SOCIAL MEDIA SECTION \*/.*?/\* MAIN CONTENT \*/', css_replacement + '        /* MAIN CONTENT */', content, flags=re.DOTALL)

html_replacement = '''
    <!-- SOCIAL MEDIA SECTION (Direkt unter dem Hero platziert) -->
    <div class="social-media-container">
        <h2 class="section-header" style="font-size: 22px; font-weight: normal;">Aktuelles aus unseren Sozialen Medien</h2>
        <div class="social-grid-wrapper">
            <div class="social-grid">
                
                <!-- Card 1 -->
                <div class="social-card">
                    <div class="social-card-img" style="background-color: #f39c12;"></div>
                    <i class="fa-brands fa-instagram social-card-icon"></i>
                    <div class="social-card-content">
                        <div class="social-card-title">Personalversammlung: Landratsamt ist am Dienstag, 15. September geschlossen</div>
                        <div class="social-card-text">Zulassungsstellen öffnen am Nachmittag</div>
                    </div>
                </div>

                <!-- Card 2 -->
                <div class="social-card">
                    <div class="social-card-img" style="background-color: #27ae60;"></div>
                    <i class="fa-brands fa-instagram social-card-icon"></i>
                    <div class="social-card-content">
                        <div class="social-card-title">Ich date meine Ausbildung: Lehrstellenbörse Neckar-Odenwald-Kreis</div>
                        <div class="social-card-text">10. Oktober 2026</div>
                    </div>
                </div>

                <!-- Card 3 -->
                <div class="social-card">
                    <div class="social-card-img" style="background-color: #c0392b;"></div>
                    <i class="fa-brands fa-instagram social-card-icon"></i>
                    <div class="social-card-content">
                        <div class="social-card-title">Ausschreibung des Zivilcouragepreises 2026 - Verleihung im April 2027</div>
                        <div class="social-card-text">Mutige Helferinnen und Helfer gesucht</div>
                    </div>
                </div>

                <!-- Card 4 -->
                <div class="social-card">
                    <div class="social-card-img" style="background-color: #7f8c8d;"></div>
                    <i class="fa-brands fa-instagram social-card-icon"></i>
                    <div class="social-card-content">
                        <div class="social-card-title">B 292: Sanierung einer Gabionenwand bei Breitenbronn</div>
                        <div class="social-card-text">K 3936 aus Richtung Obrigheim vorübergehend wieder befahrbar</div>
                    </div>
                </div>

                <!-- Card 5 -->
                <div class="social-card">
                    <div class="social-card-img" style="background-color: #2980b9;"></div>
                    <i class="fa-brands fa-instagram social-card-icon"></i>
                    <div class="social-card-content">
                        <div class="social-card-title">Neues Online-Portal für die Kfz-Zulassung (i-Kfz) ab sofort verfügbar</div>
                        <div class="social-card-text">Sparen Sie sich den Weg zur Zulassungsstelle.</div>
                    </div>
                </div>

                <!-- Card 6 -->
                <div class="social-card">
                    <div class="social-card-img" style="background-color: #8e44ad;"></div>
                    <i class="fa-brands fa-instagram social-card-icon"></i>
                    <div class="social-card-content">
                        <div class="social-card-title">Warnung vor starkem Unwetter im gesamten Landkreis</div>
                        <div class="social-card-text">Bitte beachten Sie die aktuellen Warnmeldungen des DWD.</div>
                    </div>
                </div>

                <!-- Card 7 -->
                <div class="social-card">
                    <div class="social-card-img" style="background-color: #16a085;"></div>
                    <i class="fa-brands fa-instagram social-card-icon"></i>
                    <div class="social-card-content">
                        <div class="social-card-title">Spatenstich für den neuen Radweg zwischen Buchen und Walldürn</div>
                        <div class="social-card-text">Ein weiterer Schritt für die Verkehrswende im Kreis.</div>
                    </div>
                </div>

                <!-- Card 8 -->
                <div class="social-card">
                    <div class="social-card-img" style="background-color: #d35400;"></div>
                    <i class="fa-brands fa-instagram social-card-icon"></i>
                    <div class="social-card-content">
                        <div class="social-card-title">Änderung der Öffnungszeiten der Abfallwirtschaft</div>
                        <div class="social-card-text">Ab dem kommenden Monat gelten neue Zeiten für die Deponie.</div>
                    </div>
                </div>

                <!-- Card 9 -->
                <div class="social-card">
                    <div class="social-card-img" style="background-color: #34495e;"></div>
                    <i class="fa-brands fa-instagram social-card-icon"></i>
                    <div class="social-card-content">
                        <div class="social-card-title">Stellenausschreibung: IT-Systemadministrator (m/w/d) gesucht!</div>
                        <div class="social-card-text">Werden Sie Teil unseres Teams im Landratsamt.</div>
                    </div>
                </div>

                <!-- Card 10 -->
                <div class="social-card">
                    <div class="social-card-img" style="background-color: #1abc9c;"></div>
                    <i class="fa-brands fa-instagram social-card-icon"></i>
                    <div class="social-card-content">
                        <div class="social-card-title">Erfolgreicher Abschluss der Neckar-Odenwald-Tage</div>
                        <div class="social-card-text">Wir bedanken uns bei allen Besuchern und Ausstellern!</div>
                    </div>
                </div>

            </div>
        </div>
    </div>
'''

content = re.sub(r'<!-- SOCIAL MEDIA SECTION.*?<div class="content-container">', html_replacement + '\n    <div class="content-container">', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
