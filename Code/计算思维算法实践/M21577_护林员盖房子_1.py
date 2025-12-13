m, n = map(int, input().split())
A = []
for _ in range(m):
    A.append(list(map(int, input().split())))
s = set()


def area(A, i, j, p, q):
    a = A[i][j]
    if a == 1:
        return 0
    else:
        T = True
        for k in range(p):
            list1 = A[i + k][j : j + q]
            if list1 != [0] * q:
                T = False
        if T:
            return p * q
        else:
            return 1


for i in range(m):
    for j in range(n):
        s1 = set()
        for p in range(1, m - i + 1):
            for q in range(1, n - j + 1):
                b = area(A, i, j, p, q)
                s1.add(b)
        s.add(max(s1))
print(max(s))
