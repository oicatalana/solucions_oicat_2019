import sys


for line in sys.stdin:
    v = [x for x in map(int, line.split(" ")[1:])]
    parell = 0
    senar = 0
    for x in v:
        if x%2 == 1:
            senar = max(senar, parell + x)
        else:
            parell = max(parell, senar + x)
    print(max(parell, senar))