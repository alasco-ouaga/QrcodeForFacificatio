import qrcode
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2 import PageObject
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image


# Chemin du fichier PDF d'origine
pdf_path = 'C:/Users/LE-CONCEPTEUR/Documents/dynamiccontent (2).pdf'

# Chemin vers le fichier PDF de sortie
output_pdf_path = 'C:/Users/LE-CONCEPTEUR/Documents/dynamiccontent_qr.pdf'

# Texte à encoder dans le QR code
qr_code_data = 'Insérez ici votre texte ou lien URL'

# Générer le QR code
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(qr_code_data)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white")

# Ouvrir le document PDF
pdf_reader = PdfFileReader(pdf_path)
pdf_writer = PdfFileWriter()

# Parcourir toutes les pages du PDF
for page_num in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(page_num)

    # Convertir la page en image
    img = page.extract_text()

    # Dessiner le QR code sur l'image de la page
    qr_position = (100, 100)  # Coordonnées de position du QR code sur la page
    img.paste(qr_img, qr_position)

    # Convertir l'image modifiée en page PDF
    modified_page = PageObject.createBlankPage(None, page.mediaBox.getWidth(), page.mediaBox.getHeight())
    modified_page.mergePage(img)

    # Ajouter la page modifiée au PDF de sortie
    pdf_writer.addPage(modified_page)

# Enregistrer le PDF de sortie avec le QR code ajouté
with open(output_pdf_path, 'wb') as output_file:
    pdf_writer.write(output_file)

print('QR code inséré avec succès dans le document PDF.')
