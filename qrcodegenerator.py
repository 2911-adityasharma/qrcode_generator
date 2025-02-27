import qrcode
import random

def generate_qr_code(data, filename):
    r=random.randint(1,23)
    qr = qrcode.QRCode(
        version=r,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)

if __name__ == "__main__":
    data = "https://www.youtube.com"
    filename = "qrcode.png"
    generate_qr_code(data, filename)
    print(f"QR code generated and saved as {filename}")


