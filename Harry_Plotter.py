import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

# Globale Variable für die Benutzereingabe
user_input = ""

def plot_function(func, x_range=(-10, 10), num_points=1000):
    global user_input  # Zugriff auf die globale Variable
    x = np.linspace(x_range[0], x_range[1], num_points)
    y = func(x)

    # Entferne "np." aus dem Titel
    cleaned_input = user_input.replace("np.", "")

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'{cleaned_input}')
    plt.title(f'Plot für die Funktion: {cleaned_input}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.grid(alpha=0.3)
    plt.legend()
    plt.show()

def on_plot_button_click(entry):
    global user_input  # Zugriff auf die globale Variable
    user_input = entry.get()  # Speichere die Benutzereingabe in der globalen Variable
    try:
        # Dynamisch die Funktion erstellen
        def user_function(x):
            return eval(user_input)

        # Plot der benutzerdefinierten Funktion
        plot_function(user_function, x_range=(-10, 10))
    except Exception as e:
        # Zeige eine Fehlermeldung, wenn die Eingabe ungültig ist
        messagebox.showerror("Fehler", f"Ungültige Eingabe: {e}")

# GUI erstellen
root = tk.Tk()
root.title("Harry Plotter")

# Label erstellen

# Label für die Eingabeaufforderung
label = tk.Label(root, text="Gib eine Funktion in Python-Syntax ein:")
label.pack(pady=10)

# Zusätzliches Label für die Python-Syntax-Anleitung
syntax_label = tk.Label(root, text="Python-Syntax: Potenzen mit '**' schreiben, z.B. 2 ** 3 für 2 hoch 3.\n                            Wurzeln werden mit np.sqrt(x) geschrieben.\n                            Sinus- und Cosinus-Funktionen werden mit np.sin(x) usw. erstellt.", justify="left")
syntax_label.pack(pady=2)

# Eingabefeld für die Benutzereingabe
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Button zum Plotten der Funktion
plot_button = tk.Button(root, text="Plotten", command=lambda: on_plot_button_click(entry))
plot_button.pack(pady=10)

# GUI-Event-Loop starten
root.mainloop()