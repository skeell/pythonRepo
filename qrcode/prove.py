import qrcode
data = "https://www.google.it"
file = "web.png"
img = qrcode.make(data)
img.save(file)
