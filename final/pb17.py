import sys
from collections import deque

inc_x = [ 1,  1, -1, -1 , 2,  2, -2, -2 ]
inc_y = [ 2, -2,  2, -2 , 1, -1,  1, -1 ]

f = 0
c = 0
n = 0
T = []
G = []

def veins(x, y):
    global f, c, n, T, G
    if T[x][y]:
        return
    v = c*x + y
    for k in range(8):
        x2 = x + inc_x[k]
        y2 = y + inc_y[k]
        if (x2 >= 0 and x2 < f and y2 >= 0 and y2 < c and not T[x2][y2]):
            G[v].append(c*x2 + y2)

def amplada(v):
    global f, c, n, T, G
    dist = [-1] * n
    Q = deque()
    dist[v] = 0
    Q.append(v)
    res = -33
    while len(Q) > 0:
        u = Q.popleft()
        for z in G[u]:
            if dist[z] == -1:
                res = dist[u] + 1
                dist[z] = res
                Q.append(z)
    return res

def main():
    global f, c, n, T, G

    for line in sys.stdin:
        f, c = map(int, line.split())
        TT = [False] * c
        T  = [None]  * f
        for i in range(f):
            T[i] = TT.copy()

        entrada = list(map(int, input().split()))
        for i in range(1, 2 * entrada[0] + 1, 2):
            T[entrada[i] - 1][entrada[i+1] - 1] = True

        n = f*c

        G = [None] * n
        for i in range(n):
            G[i] = []

        for x in range(f):
            for y in range(c):
                veins(x,y)

        res = 0
        for v in range(n):
            res = max(res, amplada(v))

        print(res)

main()
