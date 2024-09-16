# Install all python libraries needed which is pip install qrcode Image
import qrcode
# To create a function that collects a text and converts it to a QR Code
def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )
    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color = "black", back_color = "white")
    # Save the QR Code as an image
    img.save("qrimg.png")

# Run the function
generate_qrcode("https://www.danielmarais.com")