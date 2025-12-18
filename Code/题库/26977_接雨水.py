n = int(input())
height = list(map(int, input().split()))
res = [0] * n
l = 0
r = n - 1
hl = 0
hr = 0
while r >= l:
    hl = max(hl, height[l])
    hr = max(hr, height[r])
    if hl <= hr:
        res[l] = hl
        l += 1
    else:
        res[r] = hr
        r -= 1
S = 0
for i in range(n):
    S += res[i] - height[i]
print(S)
