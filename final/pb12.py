import sys

for line in sys.stdin:
    total, c = map(int, line.split())
    numbers = sorted(list(map(int, input().split())))
    result = int(1e9)
    for i in range(c + 1):
        aux = 0
        if i != c:
            aux += total - numbers[i] + 1
        if i > 0:
            aux += numbers[i - 1]
        result = min(result, aux)
    print(result)
