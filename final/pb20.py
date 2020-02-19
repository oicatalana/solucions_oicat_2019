import sys

tallas = ["S", "M", "L", "XL", "XXL", "XXXL"]

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def Print(y, spent, remain):
    print ("----------")
    print (y)
    for t in tallas:
        p = spent[t] - remain[t] // y
        print (t, p)

def ok(y, spent, remain):
    for t in tallas:
        p = spent[t] - remain[t] // y
        if p < 0:
            return False
    return True

def solve():
    remain = {}
    spent = {}
    for i in range(0, 6):
        xxx = input().split()
        spent[xxx[0]] = int(xxx[1])
    input()
    g = 0
    for i in range(0, 6):
        xxx = input().split()
        remain[xxx[0]] = int(xxx[1])
        spent[xxx[0]] = int(spent[xxx[0]]) - int(xxx[1])
        if i == 0:
            g = int(xxx[1])
        else:
            g = gcd(g, int(xxx[1]))

    y = 1
    best = -1
    while y * y <= g:
        if g % y == 0:
            if ok(y, spent, remain):
                Print(y, spent, remain)
                return
            if ok(g // y, spent, remain):
                best = g // y
        y = y + 1
    if best != -1:
        Print(best, spent, remain)
    else:
        print ("----------")
        print ("NO")

for line in sys.stdin:
    solve()
