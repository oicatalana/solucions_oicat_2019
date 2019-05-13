from PIL import Image, ImageDraw
import math


def minim(x, y):
    if x < y:
        return x
    else:
        return y


def distancia(x, y):
    d1 = x + y
    d2 = x + n - y - 1
    d3 = m - x - 1 + y
    d4 = m - x - 1 + n - y - 1
    return minim(minim(d1, d2), minim(d3, d4))


m = int(input())
n = int(input())
r = int(input())
g = int(input())
b = int(input())
img = Image.new('RGB', (m, n))
dib = ImageDraw.Draw(img)


for x in range(m):
    for y in range(n):
        d = distancia(x, y)
        dib.point((x, y), (d*r, d*g, d*b))


img.save("output.png")
