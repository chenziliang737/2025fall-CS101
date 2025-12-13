n = int(input())
a, b = list(map(int, input().split()))
list1 = []
for _ in range(n):
    list1.append(list(map(int, input().split())))
list1.sort(key=lambda x: x[0] * x[1])
s = 0
for t in list1:
    s = max(s, a // t[1])
    a *= t[0]
print(s)
