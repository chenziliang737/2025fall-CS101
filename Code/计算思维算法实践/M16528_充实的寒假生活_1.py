n = int(input())
list1 = []
for _ in range(n):
    a, b = map(int, input().split())
    list1.append((a, b))
list1.sort(key=lambda x: -x[1])
c = 0
s = 0
while list1:
    t = list1.pop()
    c = t[1]
    s += 1
    while list1 and list1[-1][0] <= c:
        list1.pop()
print(s)
