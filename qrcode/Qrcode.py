import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from pdf2image import convert_from_path
import os , sys
import qrcode
from PIL import Image
from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader
import shutil

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Detection falsification")
        self.geometry("800x600")
        
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
        
        self.label = tk.Label(self, text="LIEN :" , font=("arial" , 15 , "bold"))
        self.label.grid(row=0, column=0, sticky=tk.E , pady=50)

        self.entry = tk.Entry(self , font=("arial" , 15 , "bold"),border=3)
        self.entry.grid(row=0, column=1, sticky=tk.W+tk.E , padx=5)
        self.entry.bind("<Configure>", self.agrandir_entry)

        self.button = tk.Button(self, text="Valider",padx=10, font=("arial" , 11 , "bold"),bg="green",command=self.select_pdf)
        self.button.grid(row=0, column=2, sticky=tk.W)
        
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=0)
        
    def agrandir_entry(self, event):
            self.entry.config(width=(self.entry.winfo_width() + 1))

    def select_pdf(self):
        filepath = filedialog.askopenfilename(filetypes=[("Fichiers PDF", "*.pdf")])
        link = "C:/Users/LE-CONCEPTEUR/Documents/qrcode"
        images = convert_from_path(filepath)
        # Créer un nouveau PDF
        # Chemin du dossier Documents de l'utilisateur
        documents_path = os.path.expanduser("~\Documents")
        documents_link = documents_path+"\Qrcode.pdf"
        documents_link = documents_link.replace("\\", "/")
        tableau = []
        pdf = FPDF()

        # Boucle for pour insérer les indices dans le tableau
        for indice in range(10):
            tableau.append(indice)

        for i in tableau:
            folder_names = "makeQrfolder"+"_"+str(i)
            # Chemin complet du dossier à créer
            folder_path = os.path.join(documents_path, folder_names)

            # Vérifier si le dossier existe déjà
            if not os.path.exists(folder_path):
                # Créer le dossier
                os.makedirs(folder_path)
                formatted_path = folder_path.replace("\\", "/")
                print("Dossier créé avec succès :", formatted_path)
                break
            else:
                print("Le dossier existe déjà :", folder_path)
                
        for index, img in enumerate(images):
            # Générer le QR code
            data = "https://www.example.com"  # Données du QR code (URL, texte, etc.)
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(data)
            qr.make(fit=True)
            qr_image = qr.make_image(fill_color="black", back_color="white")

            # Redimensionner le QR code à la taille souhaitée
            qr_image = qr_image.resize((200, 200))  # Ajustez la taille selon vos besoins

            # Calculer les coordonnées pour placer le QR code à la fin de l'image à droite
            x = img.width - qr_image.width
            y = img.height - qr_image.height - 20
            y = 20

            # Obtenir le nom de fichier avec l'extension
            file_name ="image_"+str(index)+".jpg"
            filename = f"image_{index}.jpg"
            
            # Chemin complet du fichier de destination
            destination_path = os.path.join(formatted_path, filename)
            
            # Insérer le QR code dans l'image
            img.paste(qr_image, (x, y))  # Coordonnées de l'insertion
            
            # Enregistrer l'image avec le QR code dans le dossier de destination
            img.save(destination_path)
            
            formatted_link = formatted_path+"/"+file_name
            print(formatted_link)
            
            pdf.add_page()
            pdf.image(formatted_link, x=0, y=0, w=pdf.w, h=pdf.h)
            
        pdf.output(documents_link)
        shutil.rmtree(formatted_path)
            
            
        self.entry.delete(0, tk.END)  # Effacer le contenu précédent
        self.entry.insert(tk.END, filepath)
        
class EnregistrerPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.label = tk.Label(self, text="Bienvenue sur la page d'enregistrement")
        self.label.pack(fill="both",expand=True)
    
if __name__ == "__main__":
    app = Application()
    app.mainloop()
