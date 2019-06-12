from PIL import Image, ImageDraw


def triangle(x1, y1, x2, y2, x3, y3, col):
  dib.polygon([(x1, y1), (x2, y2), (x3, y3)], col)


def quad(x):
  return x*x


def color(x1, y1, x2, y2, x3, y3):
  qa = quad(x1 - x2) + quad(y1 - y2)
  qb = quad(x2 - x3) + quad(y2 - y3)
  qc = quad(x3 - x1) + quad(y3 - y1)
  if qa > qb:
    qa, qb = qb, qa
  if qb > qc:
    qb, qc = qc, qb
  if qa > qb:
    qa, qb = qb, qa
  if qa + qb == qc:
    return  'Blue'
  return 'Red'


c = int(input())
f = int(input())


img = Image.new('RGB', (c, f), 'Beige')
dib = ImageDraw.Draw(img)


n = int(input())
for i in range(n) :
  x1 = int(input())
  y1 = int(input())
  x2 = int(input())
  y2 = int(input())
  x3 = int(input())
  y3 = int(input())
  col = color(x1, y1, x2, y2, x3, y3)
  triangle(x1, y1, x2, y2, x3, y3, col)


img.save("output.png")