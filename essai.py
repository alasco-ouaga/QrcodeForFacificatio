import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import math

def change_button0_color():
    button0.config(bg="white")
    button1.config(bg="#2F4F4F")
    button2.config(bg="#2F4F4F")  # Changer la couleur de fond du bouton en rouge
    button3.config(bg="#2F4F4F")
    button0.config(fg="black")
    button1.config(fg="white")
    button2.config(fg="white")
    button3.config(fg="white")
    
def change_button1_color():
    button0.config(bg="#2F4F4F")
    button1.config(bg="white")
    button2.config(bg="#2F4F4F")  # Changer la couleur de fond du bouton en rouge
    button3.config(bg="#2F4F4F")
    button0.config(fg="white")
    button1.config(fg="black")
    button2.config(fg="white")
    button3.config(fg="white")
    
def change_button2_color():
    button0.config(bg="#2F4F4F")
    button1.config(bg="#2F4F4F")  # Changer la couleur de fond du bouton en rouge
    button2.config(bg="white")
    button3.config(bg="#2F4F4F")
    button0.config(fg="white")
    button1.config(fg="white")
    button2.config(fg="black")
    button3.config(fg="white")
    button2.config(window, highlightthickness=2, relief="solid")
    

def change_button3_color():
    button0.config(bg="#2F4F4F")
    button1.config(bg="#2F4F4F")  # Changer la couleur de fond du bouton en rouge
    button2.config(bg="#2F4F4F")
    button3.config(bg="white")
    button1.config(fg="white")
    button0.config(fg="white")
    button2.config(fg="white")
    button3.config(fg="black")

# Fonction pour sélectionner un fichier
def select_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        # Traitez le fichier sélectionné ici
        print("Fichier sélectionné :", filepath)

# Fonction pour sélectionner un fichier
def accueil():
    accueil_frame = tk.Frame(main_frame , bg="#3b4040")
    accueil_frame.pack(side=tk.LEFT, fill=tk.Y)
    accueil_frame.configure(width=160 ,height=400)
    accueil_frame.pack(fill="both", expand=True)
    label = tk.Label(accueil_frame,text="Visionner votre documents ici" ,  font=("Arial", 20), fg="blue", bg="yellow", justify="left")
    label.pack(anchor="w",pady=10,padx=20)
    text = tk.Text(accueil_frame,width=200, height=35)
    text.pack(pady=10 , padx=20)

window=tk.Tk()
width_of_window=1000
heidth_of_window=600

width_of_screen=window.winfo_screenwidth()
heigth_of_screen=window.winfo_screenheight()

a=((width_of_screen/2)-(width_of_window/2))
b=((heigth_of_screen/2)-(heidth_of_window/2))

window.geometry("%dx%d+%d+%d"%(width_of_window,heidth_of_window,a,b))
window.title("welcom")

# Cadre principal
main_frame = tk.Frame(window)
main_frame.pack(fill=tk.BOTH, expand=True)


# Barre de navigation à gauche
navigation_frame = tk.Frame(main_frame, bg="#2F4F4F" , width=8000)
navigation_frame.pack(side=tk.LEFT, fill=tk.Y)
navigation_frame.configure(width=160 ,height=400)

# Boutons de navigation
button0 = tk.Button(navigation_frame, text="Accueil", font=('bold' , 15) , fg='white' , bd=0 ,bg='#2F4F4F')
button0.pack(anchor=tk.W)
button0.config(width=15,text=button0["text"].upper() , command=change_button0_color)

# Boutons de navigation
button1 = tk.Button(navigation_frame, text="Ajouter", font=('bold' , 15) , fg='white' , bd=0 ,bg='#2F4F4F')
button1.pack(anchor=tk.W)
button1.config(width=15,text=button1["text"].upper() , command=change_button1_color)


button2 = tk.Button(navigation_frame, text="verifier",font=('bold' , 15) , fg='white' , bd=0 ,bg='#2F4F4F' )
button2.pack(anchor=tk.W)
button2.config(width=15,text=button2["text"].upper(),command=change_button2_color)

button3 = tk.Button(navigation_frame, text="Details", font=('bold' , 15) , fg='white' , bd=0 ,bg='#2F4F4F')
button3.pack(anchor=tk.W)
button3.config(width=15,text=button3["text"].upper() ,command=change_button3_color)



# Ajoutez votre contenu spécifique à la page ici

window.mainloop()
