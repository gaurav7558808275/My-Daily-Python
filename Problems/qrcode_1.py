import pyqrcode
import png
from pyqrcode import QRCode
from PIL import Image


s = "http://aaronhoyt.com/gfy.asp"
url = pyqrcode.create(s)
url.svg("QRcode.svg",scale = 8)
url.png("QRcode.png",scale = 8)
image = Image.open('QRcode.png')
image.show()