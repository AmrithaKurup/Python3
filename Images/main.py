from PIL import Image
mac = Image.open('ammu.JPG')
print(type(mac))
size = mac.size
print(size)
half_width = size[0] // 2
half_height = size[1] // 2
x1 = half_width - 1000
y1 = half_height - 1700
x2 = half_width + 100
y2 = half_height - 150
c = mac.crop((x1, y1, x2, y2))
mac.paste(im=c, box=(0, 0))
mac.paste(im=c, box=(4378, 0))
mac.paste(im=c, box=(0, 2100))
mac.paste(im=c, box=(4378, 2100))
mac.putalpha(120)
mac.show()
