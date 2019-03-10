from PIL import Image, ImageDraw


def dist(x1, y1, x2, y2):
    if x2 == -1: return 0
    return (abs(x1 - x2) + abs(y1 - y2))%256


n = int(input())
m = int(input())
xr = int(input())
yr = int(input())
xg = int(input())
yg = int(input())
xb = int(input())
yb = int(input())

img = Image.new('RGB', (n, m))
dib = ImageDraw.Draw(img)


for x in range (0, n):
    for y in range(0, m):
        dib.point((x, y), (dist(x, y, xr, yr), dist(x, y, xg, yg), dist(x, y, xb, yb)))


img.save("output.png")
