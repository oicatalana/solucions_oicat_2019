from PIL import Image, ImageDraw

dia = 15

c = int(input())
f = int(input())
n = int(input())

punts = [[-2 for i in range(c)] for j in range(f)]

for i in range(n):
  x = int(input()) - 1
  punts[int(input()) - 1][x] = -1

augments = [[0, 1], [1, 0], [0, -1], [-1, 0]]
augments2 = [[0, 1], [1, 0]]
component = 0

def dfs(y, x):
  global punts
  if x < 0 or y < 0 or x >= c or y >= f:
    return
  if punts[y][x] != -1:
    return
  punts[y][x] = component
  for aug in augments:
    dfs(y + aug[0], x + aug[1])

for j in range(f):
  for i in range(c):
    if (punts[j][i] == -1):
      dfs(j, i)
      component += 1

img = Image.new('RGB', (dia*c, dia*f), 'Beige')
dib = ImageDraw.Draw(img)
colors = ['Red', 'Green', 'Blue']

for j in range(f):
  for i in range(c):
    if punts[j][i] >= 0:
      col = colors[punts[j][i]%3]
      dib.ellipse([dia*i + 5, dia*j + 5, dia*i + 9, dia*j + 9], col)
      for aug in augments2:
        y = j + aug[0]
        x = i + aug[1]
        if not (x >= c or y >= f):
          if punts[j][i] == punts[y][x]:
            dib.line([(dia*i + 7, dia*j + 7), (dia*x + 7, dia*y + 7)], col)

img.save('output.png')
