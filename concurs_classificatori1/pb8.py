nor_content = [".__..", "( o>.", "///\\.", "\\V_/_"]
rev_content = ["..__.", ".<o )", "./\\\\\\", "_\\_V/"]

n = int(input())
p = int(input())
M = [[]] * 4

for i in range(4):
    M[i] = ['.'] * n

for i in range(p):
    line = input().split(" ")
    c = line[0]
    x = int(line[1])
    for j in range(4):
        for k in range(5):
            M[j][k + x] = nor_content[j][k] if c == 'D' else rev_content[j][k]

for i in range(4):
    print("".join(M[i]))


