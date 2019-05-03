from PIL import Image, ImageDraw


def pinta(i, e, d):
    if i == 0: return

    k = (e + d)//2
    dib.ellipse([e, e, k, k], c2)
    dib.ellipse([e, k + 1, k, d], c1)
    dib.ellipse([k + 1, e, d, k], c3)
    pinta(i - 1, k + 1, d)


f = input()
c1 = input()
c2 = input()
c3 = input()
n = int(input())
m = 25*2**n
img = Image.new('RGB', (m, m), f)
dib = ImageDraw.Draw(img)


pinta(n, 0, m - 1)


img.save("output.png")

