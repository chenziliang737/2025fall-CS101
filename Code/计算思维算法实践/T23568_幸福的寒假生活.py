def trans(date):
    month, day = map(int, date.split("."))
    return (month - 1) * 31 + day - 7


n = int(input())
plan = []
for _ in range(n):
    si, ei, vi = input().split()
    if trans(ei) > 44:
        continue
    plan.append([trans(si), trans(ei), int(vi)])
plan.sort(key=lambda x: (x[1], -x[0], -x[2]))
n = len(plan)
dp = [[0, 0] for _ in range(n)]
dp[0] = [0, plan[0][2]]
for i in range(1, n):
    si, ei, vi = plan[i]
    dp[i][0] = max(dp[i - 1])
    dp[i][1] = vi
    for j in range(i):
        if plan[j][1] < plan[i][0]:
            dp[i][1] = max(dp[i][1], dp[j][1] + vi)
print(max(dp[n - 1]))
