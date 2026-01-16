================================================================================
                           HARRY PLOTTER - README
================================================================================

WILLKOMMEN!
Harry Plotter ist ein interaktives Plottungs-Tool, mit dem du mathematische 
Funktionen visualisieren kannst - sowohl 2D als auch 3D!

================================================================================
                            SYNTAX & BEISPIELE
================================================================================

ALLGEMEINE REGELN:
- Nutze Python-Syntax für deine Eingaben
- Die Variable für 2D-Funktionen ist: x
- Die Variablen für 3D-Funktionen sind: x und y
- Potenzen werden mit ** geschrieben (nicht ^)
- Verwende np. für NumPy-Funktionen

================================================================================
                        2D-FUNKTIONEN BEISPIELE
================================================================================

Grundlagen:
  x**2                    → Quadratische Funktion (Parabel)
  x**3                    → Kubische Funktion
  1/x                     → Hyperbel

Trigonometrische Funktionen:
  np.sin(x)              → Sinuskurve
  np.cos(x)              → Kosinuskurve
  np.tan(x)              → Tangensfunktion

Exponential- und Logarithmusfunktionen:
  np.exp(x)              → Exponentialfunktion (e^x)
  np.log(x)              → Natürlicher Logarithmus
  np.sqrt(x)             → Quadratwurzel

Kombinationen:
  x * np.sin(x)          → Gedämpfte Schwingung
  np.exp(-x**2)          → Exponentiell abfallend
  np.sin(x) + np.cos(x)  → Kombinierte Funktionen

================================================================================
                        3D-FUNKTIONEN BEISPIELE
================================================================================

Das Programm erkennt automatisch 3D-Funktionen, wenn der Buchstabe 'y' 
vorkommt und zeigt die Funktion als 3D-Oberflächenplot!

Einfache Muster:
  x**2 + y**2                    → Paraboloid (Schüssel)
  -(x**2 + y**2)                → Umgekehrtes Paraboloid (Berg)
  x * y                          → Sattelfläche

Wellen und Schwingungen:
  np.sin(x) * np.cos(y)         → Klassisches Wellenmuster
  np.sin(np.sqrt(x**2 + y**2))  → Konzentrische Wellen
  np.sin(x) * np.sin(y)         → Schachbrettmuster

Bergige Landschaften:
  np.sin(x) + np.cos(y)         → Wellenförmige Berge
  np.sqrt(x**2 + y**2)          → Kegel
  1 / (1 + x**2 + y**2)         → Spitze in der Mitte

Gaussische Funktionen:
  np.exp(-(x**2 + y**2))                    → Glockenkurve
  np.exp(-(x**2 + y**2) * 2)               → Schärfere Glocke
  np.exp(-(x**2 + y**2) * 0.5)             → Breitere Glocke
  5 * np.exp(-(x**2 + y**2))               → Höhere Glocke

Komplexere Muster:
  np.sin(x**2 + y**2)                      → Kreisförmige Ringmuster
  np.sin(2*x) * np.cos(2*y)                → Feines Gitter
  np.exp(-(x**2 + y**2) / 2) * np.sin(5*x) → Gedämpfte Oszillationen

================================================================================
                          HILFREICHE TIPPS
================================================================================

1. FEHLERMELDUNGEN: Wenn eine Funktion nicht funktioniert, überprüfe:
   - Hast du alle Variablen verwendet (x bei 2D, x und y bei 3D)?
   - Hast du Potenzen mit ** geschrieben?
   - Hast du "np." bei NumPy-Funktionen verwendet?

2. BEREICH: Die Funktionen werden standardmäßig im Bereich -10 bis 10 
   für x und y geplottet.

3. 2D oder 3D?: Das Programm erkennt automatisch:
   - Enthält die Eingabe 'y'? → 3D-Plot
   - Keine 'y'? → 2D-Plot

4. EXPERIMENTIEREN: Versuche, eigene Kombinationen zu erstellen!
   Beispiel: np.sin(x) * np.cos(y) * np.sqrt(x**2 + y**2)

================================================================================
                            VIEL SPASS!
================================================================================
