from PIL import Image, ImageDraw


n = int(input())
diametre = [0]*n
color = ["patata"]*n

suma = 0
maxim = 0
for i in range(n):
  diametre[i] = int(input())
  color[i] = input()
  suma += diametre[i]
  maxim = max(maxim, diametre[i])

img = Image.new('RGB', (suma, maxim), 'Black')
dib = ImageDraw.Draw(img)


mig = maxim//2;
x = 0
for i in range(n):
  d = diametre[i]
  dib.ellipse([x, mig - d//2, x + d - 1, mig + d//2], color[i])
  x += d


img.save("output.png")