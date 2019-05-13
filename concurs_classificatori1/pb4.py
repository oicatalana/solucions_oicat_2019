from PIL import Image, ImageDraw


def rect(x1, y1, x2, y2, col):
    dib.polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], col)


n = int(input())
V = ['patata']*n
for i in range(n):
    V[i] = input()


img = Image.new('RGB', (100*n, 100), 'White')
dib = ImageDraw.Draw(img)


for i in range(n - 1):
    for j in range(n - 1):
        if V[j] > V[j+1]:
            a = V[j]
            V[j] = V[j+1]
            V[j+1] = a

for i in range(n):
    rect(100*i, 0, 100*i + 99, 99, V[i])


img.save("output.png")
