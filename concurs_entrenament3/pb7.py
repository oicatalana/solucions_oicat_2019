import sys


def Solve(v):
    index = dict()
    for i, x in enumerate(sorted(v)):
        index[x] = i
    
    seen = [False] * len(v)
    res = 0
    for i,x in enumerate(v):
        if not seen[i]:
            qtt = 0
            while not seen[i]:
                qtt = qtt + 1
                seen[i] = True
                i = index[x]
                x = v[i]
            res = res + qtt - 1
    print(res)

v = [x for line in sys.stdin for x in list(map(int, line.split()))]

i = 0
while i < len(v):
    Solve(v[i + 1 : i + 1 + v[i]])
    i = i + v[i] + 1
