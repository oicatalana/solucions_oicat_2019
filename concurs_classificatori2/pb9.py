import sys

def TrobaDigit(n):
    # Busca la longitud en potencies de dos que supera n.
    power = 1
    while n > power:
        power = power * 2
    
    # Tots els digits provenen del 0 inicial, nomes hem de comptar els canvis.
    res = 0
    while n != 1:
        n = n - power // 2
        res = 1 - res
        while power // 2 >= n:
            power = power // 2

    return res

for line in sys.stdin:
    n = int(line)
    print(n, ":", TrobaDigit(n))