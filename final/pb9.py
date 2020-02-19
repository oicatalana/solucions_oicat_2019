from PIL import Image, ImageDraw


M = 100


def col(c):
    if c == 'B': return 'Blue'
    if c == 'G': return 'Green'
    if c == 'O': return 'Orange'
    if c == 'P': return 'Pink'
    if c == 'R': return 'Red'
    return 'Yellow'


goal = input()
n = int(input())
mat = []
for j in range(n):
    s = input()
    fila = ['A']*4
    for i in range(4):
        fila[i] = s[i]
    mat += [fila]
    if s == goal:
        break


img = Image.new('RGB', (9*M, len(mat)*M), 'Sienna')
dib = ImageDraw.Draw(img)


for j in range(len(mat)):
    for i in range(4):
        dib.ellipse([M*i, M*j, M*(i + 1) - 1, M*(j + 1) - 1], col(mat[j][i]))

    negre = 0
    blanc = 0
    for i in range(4):
        if mat[j][i] == goal[i]:
            negre += 1
            mat[j][i] = 'M'

    blanc = 0
    for i in range(4):
        if mat[j][i] != 'M':
            k = 0
            while k < 4 and mat[j][k] != goal[i]:
                k += 1
            if k < 4:
                blanc += 1
                mat[j][k] = 'Z'

    for i in range(negre):
        dib.ellipse([M*(i + 5), M*j, M*(i + 6) - 1, M*(j + 1) - 1], 'Black')

    for i in range(blanc):
        dib.ellipse([M*(i + 5 + negre), M*j, M*(i + 6 + negre) - 1, M*(j + 1) - 1], 'White')


img.save("output.png")
