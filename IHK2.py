import tkinter as tk
from tkinter import messagebox

def calculate_grade():
    try:
        note = float(entry.get())
        if note < 0 or note > 100:
            result_label.config(text="Ungültig")
            return
        elif note >= 92:
            grade = "Sehr gut"
        elif note >= 81:
            grade = "Gut"
        elif note >= 67:
            grade = "Befriedigend"
        elif note >= 50:
            grade = "Ausreichend"
        elif note >= 30:
            grade = "Mangelhaft"
        else:
            grade = "Ungenügend"
        
        result_label.config(text="Note: {}".format(grade))
    except ValueError:
        messagebox.showerror("Fehler", "Ungültige Eingabe: Bitte geben Sie eine gültige Zahl ein.")

# GUI erstellen
root = tk.Tk()
root.title("IHK-Notenspiegel")
root.geometry("300x200")

label = tk.Label(root, text="Bitte geben Sie ein, wie viel Prozent sie erreicht haben:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

calculate_button = tk.Button(root, text="Berechnen", command=calculate_grade)
calculate_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
