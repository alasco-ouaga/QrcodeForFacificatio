import tkinter as tk

def agrandir_entry(event):
    entry.config(width=(entry.winfo_width() + 1))

fenetre = tk.Tk()

# Créer le label
label = tk.Label(fenetre, text="Label:")
label.grid(row=0, column=0, sticky=tk.E)

# Créer l'Entry
entry = tk.Entry(fenetre)
entry.grid(row=0, column=1, sticky=tk.W+tk.E)
entry.bind("<Configure>", agrandir_entry)

# Créer le Button
button = tk.Button(fenetre, text="Valider")
button.grid(row=0, column=2, sticky=tk.W)

# Configurer les colonnes pour s'étendre avec la fenêtre
fenetre.columnconfigure(0, weight=0)
fenetre.columnconfigure(1, weight=1)
fenetre.columnconfigure(2, weight=0)

fenetre.mainloop()
