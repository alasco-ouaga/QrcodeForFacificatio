import PyPDF2
import qrcode
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def add_qr_code_to_pdf(input_pdf_path, output_pdf_path, qr_content):
    # Ouvrir le document PDF existant
    with open(input_pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        pdf_writer = PyPDF2.PdfFileWriter()

        # Générer le QR code
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=4)
        qr.add_data(qr_content)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")

        # Parcourir chaque page du document PDF
        for page_number in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_number)

            # Convertir la page PDF en image
            c = canvas.Canvas("page_tmp.pdf", pagesize=letter)
            c.drawImage(input_pdf_path, 0, 0, width=letter[0], height=letter[1])
            c.save()

            # Charger la page PDF convertie en image
            with open("page_tmp.pdf", "rb") as page_file:
                page_pdf_reader = PyPDF2.PdfFileReader(page_file)
                page_pdf = page_pdf_reader.getPage(0)

                # Créer une nouvelle page avec le QR code
                page_pdf.mergeTranslatedPage(qr_image, page_pdf.mediaBox.getWidth() - qr_image.width - 10, 10)  # Modifier les coordonnées selon vos besoins

                # Ajouter la page modifiée au nouveau document PDF
                pdf_writer.addPage(page_pdf)

        # Enregistrer le nouveau document PDF avec les QR codes ajoutés
        with open(output_pdf_path, "wb") as output_file:
            pdf_writer.write(output_file)

# Chemin du document PDF d'entrée
input_pdf_path = "C:/Users/LE-CONCEPTEUR/Documents/tesPdf/devoir_enonce.pdf"

# Chemin du document PDF de sortie avec les QR codes ajoutés
output_pdf_path = "C:/Users/LE-CONCEPTEUR/Documents/tesPdf/devoir_enonce_1.pdf"

# Contenu du QR code
qr_content = "Mon QR code"

# Ajouter les QR codes au document PDF
add_qr_code_to_pdf(input_pdf_path, output_pdf_path, qr_content)















