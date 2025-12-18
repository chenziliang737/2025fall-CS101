n = int(input())
a, b = map(int, input().split())
nums = []
for _ in range(n):
    nums.append(tuple(map(int, input().split())))
nums.sort(key=lambda x: x[0] * x[1])
S = 0
c = a
for t in nums:
    x, y = t
    S = max(S, c // y)
    c *= x
print(S)
