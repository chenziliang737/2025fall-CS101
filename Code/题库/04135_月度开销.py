N, M = map(int, input().split())
costs = []
for _ in range(N):
    costs.append(int(input()))


def check(d):
    m = 0
    cd = 0
    for cost in costs:
        if cost > d:
            return False
        if cd + cost <= d:
            cd += cost
        else:
            m += 1
            cd = cost
    m += 1
    return m <= M


l = max(costs) - 1
r = sum(costs)
while r - l > 1:
    mid = (l + r + 1) // 2
    if check(mid):
        r = mid
    else:
        l = mid
print(r)
