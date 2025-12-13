from collections import defaultdict

N = int(input())
a = list(map(int, input().split()))
dict1 = defaultdict(int)
x = 0
for i in range(N):
    dict1[i - a[i]] = max(dict1[i - a[i]], i + a[i])
    if i - a[i] <= 0:
        x = max(x, dict1[i - a[i]])
y = x
s = 1
for i in range(N):
    x = max(x, dict1[i])
    if i == y + 1:
        y = x
        s += 1
print(s)
