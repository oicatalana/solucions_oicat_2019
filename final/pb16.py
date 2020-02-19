def rec(res, usat, length):
    if length == n:
        print("".join(res))
        return

    for i in range(n):
        if not usat[i] and abs(i - length) >= d:
            res[length] = chr(ord('A') + i)
            usat[i] = True
            rec(res, usat, length + 1)
            usat[i] = False


n = int(input())
d = int(input())

res = ["" for i in range(n)]
usat = [False for i in range(n)]

rec(res, usat, 0)
