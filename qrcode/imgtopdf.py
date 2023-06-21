from fpdf import FPDF

def create_pdf_with_images(image_paths, output_pdf_path):
    pdf = FPDF()

    for image_path in image_paths:
        pdf.add_page()
        pdf.image(image_path, x=0, y=0, w=pdf.w, h=pdf.h)  # Ajouter l'image avec les dimensions et les coordonnées appropriées

    pdf.output(output_pdf_path)

# Liste des chemins vers les deux images
image_paths = ["C:/Users/LE-CONCEPTEUR/Documents/qrcode/img_0.jpg", "C:/Users/LE-CONCEPTEUR/Documents/qrcode/img_1.jpg"]

# Chemin de sortie du fichier PDF
output_pdf_path = "C:/Users/LE-CONCEPTEUR/Desktop/getPdf/output.pdf"

# Créer le fichier PDF et ajouter les images
create_pdf_with_images(image_paths, output_pdf_path)
