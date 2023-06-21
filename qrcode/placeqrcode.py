import qrcode
from PIL import Image

# Générer le QR code
data = "https://www.example.com"  # Données du QR code (URL, texte, etc.)
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
qr_image = qr.make_image(fill_color="black", back_color="white")

# Charger l'image de fond
background_image = Image.open("C:/Users/LE-CONCEPTEUR/Documents/image/output_0.jpg")

# Redimensionner le QR code à la taille souhaitée
qr_image = qr_image.resize((200, 200))  # Ajustez la taille selon vos besoins

# Calculer les coordonnées pour placer le QR code à la fin de l'image à droite
x = background_image.width - qr_image.width
y = background_image.height - qr_image.height

# Superposer le QR code sur l'image de fond
background_image.paste(qr_image, (x, y))

# Enregistrer l'image modifiée
background_image.save("C:/Users/LE-CONCEPTEUR/Documents/qrcode/output_.jpg")
