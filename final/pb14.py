import sys

def ExisteixAresta(x1, y1, y2):
    if (x1 + y1) % 2 == 0:
        return y1 < y2
    return y1 > y2

for line in sys.stdin:
    x1, y1, x2, y2 = map(int, line.split(" "))

    diff_x = abs(x2 - x1)    
    diff_y = abs(y2 - y1)

    if diff_y > diff_x:
        mov_x = diff_y - 1 - diff_x
        if not ExisteixAresta(x1, y1, y2):
            mov_x += 1
        res = diff_x + diff_y + mov_x + (0 if (diff_x + mov_x) % 2 == (x2 - x1) % 2 else 1)
    else:
        res = diff_x + diff_y

    print(res)
