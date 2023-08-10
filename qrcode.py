import qrcode
data = "https://gayathri-portfolio-project.netlify.app/"
qr = qrcode.QRCode(version = 1,
				box_size = 10,
				border = 5)
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill_color = 'blue',
					back_color = 'white')

img.save('MyQRCode2.png')
