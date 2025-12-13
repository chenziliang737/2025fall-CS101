n, k = map(int, input().split())
inp = list(map(int, input().split()))
a = n * 2
b = n
for i in range(k):
    x = inp[i] // 4
    y = min(x, b)
    b -= y
    inp[i] -= y * 4
a += b
for i in range(k):
    x = inp[i] // 2
    y = min(x, a)
    a -= y
    inp[i] -= y * 2
if sum(inp) <= (a + b):
    print("YES")
else:
    print("NO")
