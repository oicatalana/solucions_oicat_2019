import sys

def Collatz(n):
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1

for line in sys.stdin:
    n = int(line)
    n = Collatz(n)
    while n % 2 == 0:
        n = Collatz(n)
    print(n)