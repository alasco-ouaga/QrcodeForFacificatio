import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import PyPDF2

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Detection falsification")
        
        # Créer la barre de navigation
        self.navigation_bar = ttk.Treeview(self)
        self.navigation_bar.pack(side="left", fill="y")

        # Ajouter les pages à la barre de navigation
        self.navigation_bar.tag_configure("big_font", font=("Arial", 12))
        self.navigation_bar.insert("", "end", text="Accueil", values=("accueil_page",), tags=("big_font",))
        self.navigation_bar.insert("", "end", text="Enregistrer", values=("enregistrer_page",), tags=("big_font",))

        # Associer les pages aux boutons de la barre de navigation
        self.navigation_bar.bind("<<TreeviewSelect>>", self.show_selected_page)

        # Créer les pages
        self.accueil_page = AccueilPage(self)
        self.enregistrer_page = EnregistrerPage(self)

        # Afficher la page d'accueil par défaut
        self.show_page(self.accueil_page)

    def show_selected_page(self, event):
        selected_item = self.navigation_bar.selection()
        page_id = self.navigation_bar.item(selected_item)["values"][0]
        
        if page_id == "accueil_page":
            self.show_page(self.accueil_page)
        elif page_id == "enregistrer_page":
            self.show_page(self.enregistrer_page)

    def show_page(self, page):
        if hasattr(self, "current_page"):
            self.current_page.pack_forget()
        
        page.pack(fill="both", expand=True)
        self.current_page = page

class AccueilPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,bg="#c3c3c3", highlightbackground="black", highlightthickness=1)  # Ajout du fond rouge au cadre principal
        self.pack(fill="both", expand=True)
        
        self.text = tk.Text()

        # Champ d'entrée pour le chemin du fichier PDF
        self.file_entry = tk.Entry(self)
        self.file_entry.pack(side="left", padx=10, pady=10)

        # Bouton pour sélectionner le fichier PDF
        self.select_button = tk.Button(self, text="Sélectionner", command=self.select_pdf)
        self.select_button.pack(side="left", padx=5)

    def select_pdf(self):
        filepath = filedialog.askopenfilename(filetypes=[("Fichiers PDF", "*.pdf")])
        self.file_entry.delete(0, tk.END)  # Effacer le contenu précédent
        self.file_entry.insert(tk.END, filepath)



class EnregistrerPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.label = tk.Label(self, text="Bienvenue sur la page d'enregistrement")
        self.label.pack(fill="both", expand=True)
    

if __name__ == "__main__":
    app = Application()
    app.mainloop()
