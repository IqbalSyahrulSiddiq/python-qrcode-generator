# Import QRCode from pyqrcode
import pyqrcode
import random
import png
from pyqrcode import QRCode


# String which represents the QR code
s = "www.google.com"
fileName = random.randint(1111111111,9999999999)
fileNamePass = str(fileName)

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg('C:/xampp/htdocs/product/python-qrcode-generator/qrcode-result/QRcodeImageResult - ' + fileNamePass +'.svg', scale = 8)

# Create and save the png file naming "myqr.png"
url.png('C:/xampp/htdocs/product/python-qrcode-generator/qrcode-result/QRcodeImageResult - ' + fileNamePass +'.png', scale = 6)
