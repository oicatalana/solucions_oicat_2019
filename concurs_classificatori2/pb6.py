from PIL import Image, ImageDraw


cella = 75


def rect(x1, y1, x2, y2, col):
  dib.polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], col)


def cercle(x, y, col):
  dib.ellipse([cella*x + 25, cella*y + 25, cella*x + 49, cella*y + 49], col)


c = int(input())
f = int(input())


img = Image.new('RGB', (cella*c, cella*f), 'Beige')
dib = ImageDraw.Draw(img)


mat = []
for j in range(f):
    fila = [0]*c
    mat += [fila]

mat[0][0] = 1
cercle(0, 0, 'Black')
mat[f-1][c-1] = 1
cercle(c - 1, f - 1, 'Black')
n = int(input())
for r in range(n):
  x = int(input()) - 1
  y = int(input()) - 1
  mat[y][x] = 1
  cercle(x, y, 'Black')

x = 0
y = 0
color = ''
while color == '':
  if x == c - 1 and y == f - 1:
    color = 'Green'
  elif x < c - 1 and mat[y][x+1]:
    x += 1
  elif y < f - 1 and mat[y+1][x]:
    y += 1
  else:
    color = 'Red'

x = 0
y = 0
fi = False
while not fi:
  cercle(x, y, color)
  if x == c - 1 and y == f - 1:
    fi = True
  elif x < c - 1 and mat[y][x+1]:
    rect(cella*x + cella//2, cella*y + 35, cella*x + 3*cella//2, cella*y + 39, color)
    x += 1
  elif y < f - 1 and mat[y+1][x]:
    rect(cella*x + 35, cella*y + cella//2, cella*x + 39, cella*y + 3*cella//2, color)
    y += 1
  else:
    fi = True


img.save("output.png")