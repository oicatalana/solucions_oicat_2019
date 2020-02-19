from PIL import Image, ImageDraw


n = int(input())
m = int(input())
x = int(input())
y = int(input())
c = int(input())
p = int(input())


img = Image.new('RGB', [n, m])
dib = ImageDraw.Draw(img)


def pacman_distance(a, b):
    a1 = abs(x - a)
    a2 = abs(y - b)
    return min(a1, n - a1) + min(a2, m - a2)

def rainbow(z):
    if z < 255:
        return (255, z, 0)
    z -= 255
    if z < 255:
        return (255 - z, 255, 0)
    z -= 255
    if z < 255:
        return (0, 255, z)
    z -= 255
    if z < 255:
        return (0, 255 - z, 255)
    z -= 255
    if z < 255:
        return (z, 0, 255)
    z -= 255
    return (255, 0, 255 - z)

#mx = 0
for i in range (n):
    for j in range (m):
        z = 1529 - c*pacman_distance(i, j)
#        mx = max(mx, z)
        dib.point([i,j], rainbow(z))
#print(mx)

dib.pieslice([x - p, y - p, x + p, y + p], 45, 315, 'Yellow')


img.save("output.png")
