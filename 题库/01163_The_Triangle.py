N = int(input())
a = int(input())
dp1 = [a]
for i in range(2, N + 1):
    list1 = list(map(int, input().split()))
    dp2 = [0] * i
    dp2[0] = dp1[0] + list1[0]
    dp2[-1] = dp1[-1] + list1[-1]
    for j in range(1, i - 1):
        dp2[j] = list1[j] + max(dp1[j - 1], dp1[j])
    dp1 = dp2[:]
print(max(dp2))
