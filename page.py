import qrcode
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image
from reportlab.lib.utils import ImageReader


# Générer le QR code
data = "https://www.example.com"  # Les données que vous souhaitez encoder dans le QR code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white")

# Charger le fichier PDF existant
pdf_path = "C:/Users/LE-CONCEPTEUR/Documents/tesPdf/devoir_enonce.pdf"
output_path = "C:/Users/LE-CONCEPTEUR/Documents/tesPdf/devoir5.pdf"
pdf = PdfFileReader(pdf_path)
output_pdf = PdfFileWriter()

# Parcourir les pages du PDF existant
for page_num in range(pdf.getNumPages()):
    # Récupérer les dimensions de la page PDF
    existing_page = pdf.getPage(page_num)
    page_width = existing_page.mediaBox[2]
    page_height = existing_page.mediaBox[3]

    # Convertir l'image du QR code en une image PIL
    qr_img_pil = qr_img.get_image()

    # Redimensionner l'image du QR code selon les dimensions de la page
    qr_img_pil = qr_img_pil.resize((100, 100))  # Réglez les dimensions selon vos besoins

    # Créer un canevas ReportLab pour la page PDF
    overlay = canvas.Canvas("overlay.pdf", pagesize=(page_width, page_height))
    x_pos = page_width - qr_img_pil.width -10
    y_pos = page_height - qr_img_pil.height  -10
     # Position horizontale du QR code (ici, à 10 points du bord droit)
    y_pos = 10  # Position verticale du QR code (ici, à 10 points du bord bas)
    overlay.drawImage(ImageReader(qr_img_pil), x_pos, y_pos, qr_img_pil.width, qr_img_pil.height)
    overlay.save()

    # Fusionner la page existante avec le QR code
    merged_page = PdfFileReader("overlay.pdf").getPage(0)
    merged_page.mergePage(existing_page)

    # Ajouter la page modifiée au nouveau PDF de sortie
    output_pdf.addPage(merged_page)

# Enregistrer le nouveau PDF avec le QR code ajouté
with open(output_path, "wb") as f:
    output_pdf.write(f)
