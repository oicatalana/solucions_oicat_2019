from PIL import Image, ImageDraw
from math import sin


m = int(input())
n = int(input())
dr = int(input())
db = int(input())
img = Image.new('RGB', (m, n))
dib = ImageDraw.Draw(img)


def r(i, j):
    return int(127*(1 + sin(i/dr)))


def b(i, j):
    return int(127*(1 + sin(j/db)))


for i in range(m):
    for j in range(n):
        dib.point((i, j), (r(i, j), 0, b(i, j)))


img.save("output.png")

