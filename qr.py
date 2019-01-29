import qrcode
img = qrcode.make("{'placa':'QWR1234','hora':'18-12-2018 17:08:00'}")
img.save("QWR1234-20181812-170800.jpg")
img.show()