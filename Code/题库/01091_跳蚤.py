N, M = map(int, input().split())
p = []
M1 = M
i = 2
while i ** 2 <= M1:
    if M1 % i == 0:
        p.append(i)
        while M1 % i == 0:
            M1 = M1 // i
    i += 1
if M1 > 1:
    p.append(M1)
n = len(p)
ans = 0
for i in range(1 << n):
    d = 1
    sgn = 1
    for j in range(n):
        if i & (1 << j):
            d *= p[j]
            sgn *= -1
    ans += sgn * (M // d) ** N
print(ans)
