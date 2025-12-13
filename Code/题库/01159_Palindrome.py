N = int(input())
s = input()
if N == 1:
    print(0)
    exit()
dp1 = [0] * N
dp2 = [0] * (N - 1)
for i in range(N - 1):
    if s[i] == s[i + 1]:
        dp2[i] = 0
    else:
        dp2[i] = 1
for d in range(2, N):
    dp3 = [0] * (N - d)
    for i in range(N - d):
        if s[i] == s[i + d]:
            dp3[i] = dp1[i + 1]
        else:
            dp3[i] = min(dp2[i], dp2[i + 1]) + 1
    dp1 = dp2[:]
    dp2 = dp3[:]
print(dp2[0])
