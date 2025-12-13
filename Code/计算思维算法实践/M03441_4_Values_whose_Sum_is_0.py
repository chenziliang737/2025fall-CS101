n = int(input())
A = {}
B = {}
C = {}
D = {}
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A[a] = A.get(a, 0) + 1
    B[b] = B.get(b, 0) + 1
    C[c] = C.get(c, 0) + 1
    D[d] = D.get(d, 0) + 1
dict1 = dict()
for a in A.keys():
    for b in B.keys():
        dict1[a + b] = dict1.get(a + b, 0) + A[a] * B[b]
A.clear()
B.clear()
s = 0
for c in C.keys():
    for d in D.keys():
        if -(c + d) in dict1.keys():
            s += C[c] * D[d] * dict1[-(c + d)]
print(s)
