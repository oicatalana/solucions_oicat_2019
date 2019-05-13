[x1, y1, y2, x2] = map(int, input().split(" "))

if x1 + x2 > y1 + y2:
    print("X")
elif x1 + x2 < y1 + y2:
    print("Y")
elif x2 > y1:
    print("X")
elif x2 < y1:
    print("Y")
else:
    print("P")

