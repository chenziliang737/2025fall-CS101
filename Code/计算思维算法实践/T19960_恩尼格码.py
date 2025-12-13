L = []
for _ in range(6):
    L.append(list(map(int, input().split())))
M = []
for _ in range(6):
    M.append(list(map(int, input().split())))
R = []
for _ in range(6):
    R.append(list(map(int, input().split())))
F = {}
for _ in range(3):
    a, b = map(int, input().split())
    F[a] = b
    F[b] = a
C = [0, 0]


def change(x, A, d):
    for t in A:
        if x == t[d]:
            return t[1 - d]


def encode(x, L, M, R, F):
    x1 = change(x, L, 0)
    x2 = change(x1, M, 0)
    x3 = change(x2, R, 0)
    x4 = F[x3]
    x5 = change(x4, R, 1)
    x6 = change(x5, M, 1)
    y = change(x6, L, 1)
    return y


def turn(A):
    for i in range(6):
        for j in range(2):
            A[i][j] = A[i][j] % 6 + 1


def turnall(L, M, R, C):
    if C[0] == 5 and C[1] == 5:
        C[0] = 0
        C[1] = 0
        turn(L)
        turn(M)
        turn(R)
    elif C[0] == 5:
        C[0] = 0
        C[1] += 1
        turn(L)
        turn(M)
    else:
        C[0] += 1
        turn(L)


def main():
    str1 = input()
    str2 = ""
    for a in str1:
        x = ord(a) - 96
        y = encode(x, L, M, R, F)
        str2 += chr(y + 96)
        turnall(L, M, R, C)
    print(str2)


main()
