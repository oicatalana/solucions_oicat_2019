from PIL import Image, ImageDraw


def rect(x1, y1, x2, y2, col):
    dib.polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], col)


f = input()
n = int(input())
a = int(input())
r1 = int(input())
g1 = int(input())
b1 = int(input())
r2 = int(input())
g2 = int(input())
b2 = int(input())
img = Image.new('RGB', (a*n, a*n), f)
dib = ImageDraw.Draw(img)


for i in range(n):
    e = a*i
    d = e + a - 1
    y = a*(n - i - 1)
    rect(e, e, d, d, (r1, g1, b1))
    rect(e, y, d, y + a - 1, (r2, g2, b2))

# si la n es senar, cal (tornar a) escriure el quadrat del mig
if (n%2 == 1):
    x1 = a*(n//2)
    x2 = x1 + a - 1
    rect(x1, x1, x2, x2, ((r1 + r2)//2, (g1 + g2)//2, (b1 + b2)//2))


img.save("output.png")
