import tkinter as tk
from tkinter import messagebox
import random

# Functie om een compatibiliteitsscore te berekenen op basis van overeenkomende letters
def calculate_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    # Bereken de overeenkomende letters
    common_letters = set(name1) & set(name2)
    score = (len(common_letters) * 10) + random.randint(0, 50)
    return min(score, 100)  # Zorg dat de score niet hoger dan 100 is

# Functie om de love score te berekenen en resultaat te tonen
def test_love():
    name1 = entry_name1.get()
    name2 = entry_name2.get()

    # Controleer of beide namen zijn ingevuld
    if not name1 or not name2:
        messagebox.showwarning("Waarschuwing", "Voer beide namen in om de test te doen!")
        return

    # Bereken de score en toon het resultaat
    score = calculate_score(name1, name2)
    result_text = f"{name1} en {name2} hebben een compatibiliteitsscore van {score}%!"
    
    if score > 85:
        result_text += "\n😍 Jullie zijn bijna perfect voor elkaar!"
    elif score > 60:
        result_text += "\n😊 Er is een goede kans op een mooie connectie!"
    elif score > 30:
        result_text += "\n😐 Er is wat werk nodig, maar het kan slagen!"
    else:
        result_text += "\n😕 Misschien passen jullie beter als vrienden."
    
    # Toon het resultaat in een pop-up venster
    messagebox.showinfo("Love Tester Resultaat", result_text)

# Maak het hoofdvenster
root = tk.Tk()
root.title("💖 Love Tester 💖")
root.geometry("400x300")
root.config(bg="#FFC0CB")  # Lichte roze achtergrond voor een romantische sfeer

# Titel label
title_label = tk.Label(root, text="💖 Love Tester 💖", font=("Arial", 24, "bold"), bg="#FFC0CB", fg="#FF69B4")
title_label.pack(pady=10)

# Naam invoer labels en velden
label_name1 = tk.Label(root, text="Naam van eerste persoon:", bg="#FFC0CB", font=("Arial", 12))
label_name1.pack()
entry_name1 = tk.Entry(root, font=("Arial", 12), width=20)
entry_name1.pack(pady=5)

label_name2 = tk.Label(root, text="Naam van tweede persoon:", bg="#FFC0CB", font=("Arial", 12))
label_name2.pack()
entry_name2 = tk.Entry(root, font=("Arial", 12), width=20)
entry_name2.pack(pady=5)

# Test Love knop
test_button = tk.Button(root, text="Test Love ❤️", font=("Arial", 14, "bold"), bg="#FF69B4", fg="white", command=test_love)
test_button.pack(pady=20)

# Achtergrond afbeelding toevoegen (optioneel)
# Je kunt een afbeelding als achtergrond gebruiken als je die hebt.
# Plaats een afbeelding in dezelfde map en noem deze "background.png".

try:
    bg_image = tk.PhotoImage(file="background.png")
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)
except Exception as e:
    print("Geen achtergrondafbeelding gevonden. Je kunt 'background.png' toevoegen aan de map voor een achtergrond.")

# Start de GUI
root.mainloop()
