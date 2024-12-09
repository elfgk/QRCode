import pyqrcode

url = input("URL giriniz: ")
# QR kodu oluşturma
qr_code = pyqrcode.create(url)
try:
    qr_code.svg('qrcode.svg', scale=5)
except Exception as e:
    print(f"Hata: {e}")