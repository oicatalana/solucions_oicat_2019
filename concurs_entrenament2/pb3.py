from PIL import Image, ImageDraw


def rect(x1, y1, x2, y2, col):
    dib.polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], col)


n = int(input())
x = int(input())
y = int(input())
z = int(input())
img = Image.new('RGB', (n, n), 'Black')
dib = ImageDraw.Draw(img)


m = n/2
mx = (x + z)/2
my = (y + z)/2
x1 = m - mx
x2 = m - mx + x - 1
y1 = m - my
y2 = m - my + y - 1
rect(x1, y1, x2, y2, 'White')
dib.polygon([(x1 + 1, y2 + 1), (x2 + 1, y2 + 1), (x2 + z, y2 + z), (x1 + z, y2 + z)], 'Silver')
dib.polygon([(x2 + 1, y1), (x2 + 1, y2), (x2 + z, y2 + z - 1), (x2 + z, y1 + z - 1)], 'Grey')


img.save("output.png")

