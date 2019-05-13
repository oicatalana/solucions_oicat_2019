import sys

for line in sys.stdin:
    n = int(line)
    v = [0] * n
    len = 1
    while len < n:
        j = 0
        while j < len and j + len < n:
            v[j + len] = 1 - v[j]
            j = j + 1
        len = len * 2
    
    print(''.join(map(str, v)))
