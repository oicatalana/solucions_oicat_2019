from PIL import Image, ImageDraw


x1 = int(input())
y1 = int(input())
d1 = int(input())
x2 = int(input())
y2 = int(input())
d2 = int(input())
img = Image.new('RGB', (500, 500), 'Black')
dib = ImageDraw.Draw(img)


dib.ellipse([x1, y1, x1 + d1 - 1, y1 + d1 - 1], 'White')
dib.ellipse([x2, y2, x2 + d2 - 1, y2 + d2 - 1], 'Black')


img.save("output.png")
