T = int(input())
for _ in range(T):
    N = int(input())
    list1 = list(map(int, input().split()))
    dp1 = [0] * N
    m = float("inf")
    s = 0
    for i in range(N):
        if list1[i] < m:
            m = list1[i]
        elif list1[i] - m > s:
            s = list1[i] - m
        dp1[i] = s
    dp2 = [0] * N
    M = -float("inf")
    s = 0
    for j in range(N - 1, -1, -1):
        if list1[j] > M:
            M = list1[j]
        elif M - list1[j] > s:
            s = M - list1[j]
        dp2[j] = s
    print(max(map(lambda x: dp1[x] + dp2[x], range(N))))
