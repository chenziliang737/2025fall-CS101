N, S = map(int, input().split())
cost = float("inf")
ans = 0
for _ in range(N):
    c, y = map(int, input().split())
    cost = min(cost + S, c)
    ans += cost * y
print(ans)
