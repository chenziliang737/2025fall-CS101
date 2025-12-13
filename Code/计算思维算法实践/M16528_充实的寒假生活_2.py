n = int(input())
list1 = []
for _ in range(n):
    a, b = map(int, input().split())
    list1.append((a, b))
list1.sort()
dp = [1] * n
for i in range(n - 1, -1, -1):
    t = list1[i]
    list2 = [1]
    for j in range(i + 1, n):
        if list1[j][0] > list1[i][1]:
            list2.append(dp[j] + 1)
    dp[i] = max(list2)
print(max(dp))
