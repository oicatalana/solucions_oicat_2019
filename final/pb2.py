def EsPrimer(n):
    x = 2
    while x * x <= n:
        if n % x == 0:
            return False
        x = x + 1
    return True

result = 1
for i in range(1, 65):
    n = 2 ** i + 1
    if EsPrimer(n):
        print(n)
        result = result * n

print("Producte:", result)
