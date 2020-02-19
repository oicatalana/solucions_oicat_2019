from PIL import Image, ImageDraw

m = 50

veredicte = input()

c1 = 'Black'
c2 = 'Black'
c3 = 'Black'

if veredicte == "AC":
    c3 = 'Green'
elif veredicte == "PE":
    c2 = 'Yellow'
else:
    c1 = 'Red'

img = Image.new('RGB', [12*m, 18*m], 'SkyBlue')
dib = ImageDraw.Draw(img)

dib.polygon([(7*m, 8*m), (12*m - 1, 8*m), (12*m - 1, 10*m - 1), (7*m, 10*m - 1)], 'DimGrey')

dib.polygon([(m, m), (7*m - 1, m), (7*m - 1, 17*m - 1), (m, 17*m - 1)], 'Orange')

dib.ellipse([2*m, 2*m, 6*m - 1, 6*m - 1], c1)
dib.ellipse([2*m, 7*m, 6*m - 1, 11*m - 1], c2)
dib.ellipse([2*m, 12*m, 6*m - 1, 16*m - 1], c3)

img.save("output.png")

