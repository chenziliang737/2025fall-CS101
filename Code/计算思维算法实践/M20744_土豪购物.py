list1 = list(map(int, input().strip().split(",")))
n = len(list1)
if n == 1:
    print(list1[0])
else:
    dp1 = [0] * n
    dp1[0] = list1[0]
    for i in range(1, n):
        dp1[i] = max(list1[i], dp1[i - 1] + list1[i])
    dp2 = [0] * n
    dp2[-1] = list1[-1]
    for j in range(n - 2, -1, -1):
        dp2[j] = max(list1[j], dp2[j + 1] + list1[j])
    s = -float("inf")
    for i in range(n):
        s = max(s, dp1[i])
    for j in range(n - 2):
        s = max(s, dp1[j] + dp2[j + 2])
    print(s)
