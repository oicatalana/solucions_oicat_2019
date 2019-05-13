
from PIL import Image, ImageDraw


def rect(x1, y1, x2, y2, col):
    dib.polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], col)


def ok():
    if mat[0][0] == 2 and mat[0][1] == 2 and mat[0][2] == 2: return True
    if mat[1][0] == 2 and mat[1][1] == 2 and mat[1][2] == 2: return True
    if mat[2][0] == 2 and mat[2][1] == 2 and mat[2][2] == 2: return True
    if mat[0][0] == 2 and mat[1][0] == 2 and mat[2][0] == 2: return True
    if mat[0][1] == 2 and mat[1][1] == 2 and mat[2][1] == 2: return True
    if mat[0][2] == 2 and mat[1][2] == 2 and mat[2][2] == 2: return True
    if mat[0][0] == 2 and mat[1][1] == 2 and mat[2][2] == 2: return True
    if mat[0][2] == 2 and mat[1][1] == 2 and mat[2][0] == 2: return True
    return False


def busca():
    for j in range(3):
        for i in range(3):
            if mat[j][i] == 0:
                mat[j][i] = 2
                if (ok()): return
                mat[j][i] = 0


mat = []
for j in range(3):
    fila = [-1]*3
    s = input()
    for i in range(3):
        c = s[i]
        if c == 'B': fila[i] = 1
        elif c == 'R': fila[i] = 2
        else: fila[i] = 0
    mat += [fila]


img = Image.new('RGB', (340, 340), 'White')
dib = ImageDraw.Draw(img)


for j in range(4):
    y = 110*j
    rect(0, y, 339, y + 9, 'Green')


for i in range(4):
    x = 110*i
    rect(x, 0, x + 9, 339, 'Green')


busca()


col = ['Black', 'Blue', 'Red']
for j in range(3):
    for i in range(3):
        x = 110*i + 10
        y = 110*j + 10
        k = mat[j][i]
        if k > 0:
            dib.ellipse([x, y, x + 99, y + 99], col[k])


img.save("output.png")

