from PIL import Image, ImageDraw
import math


c1 = input()
c2 = input()
r = int(input())
v1 = float(input())
v2 = float(input())


img = Image.new('RGB', (801, 801), c1)
dib = ImageDraw.Draw(img)


pi = math.pi
a1 = 0.0
a2 = 0.0
while a1 < 360:
    x = 400 + 300*math.cos(pi*a1/180) + r*math.cos(pi*a2/180)
    y = 400 + 300*math.sin(pi*a1/180) + r*math.sin(pi*a2/180)
    dib.point((x, y), c2)
    a1 += v1
    a2 += v2
print(a1)


img.save("output.png")
