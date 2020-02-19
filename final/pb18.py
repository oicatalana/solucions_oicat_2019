import sys

for line in sys.stdin:
    f, c = map(int, line.split())
    mapa = [input() for i in range(f)]
    M = [[1 if mapa[i][j] == '.' else 0 for j in range(c)] for i in range(f)]

    result = 0
    for i in range(f):
        if i != 0:
            for j in range(c):
                if M[i][j] == 1:
                    M[i][j] += M[i-1][j]
                else:
                    M[i][j] = 0

        stack = [[-1,-1]]
        last = 0
        M[i].append(0)
        for j in range(c + 1):
            if last < M[i][j]:
                stack.append([M[i][j], j])
            elif last > M[i][j]:
                while stack[-1][0] > M[i][j]:
                    x, ini = stack[-1]
                    stack.pop()
                    result = max(result, x * (j - ini))
                    last_pos = ini
                stack.append([M[i][j], last_pos])
            last = M[i][j]
    print(result)
