import os

# Chemin du dossier Documents de l'utilisateur
documents_path = os.path.expanduser("~\Documents")

tableau = [] 

# Boucle for pour insérer les indices dans le tableau
for indice in range(10):
    tableau.append(indice)


# Parcourir la liste des noms de dossiers
i=2
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
