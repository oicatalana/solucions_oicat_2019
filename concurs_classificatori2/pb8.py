
def LlegeixSamarretes(contenidor):
    for i in range(6):
        tokens = input().split(" ")
        contenidor[tokens[0]] = int(tokens[1])

comprades = dict()
restants = dict()

LlegeixSamarretes(comprades)
input()
LlegeixSamarretes(restants)

for talla in ["S", "M", "L", "XL", "XXL", "XXXL"]:
    print(talla, max(0, comprades[talla] - 2 * restants[talla]))
    