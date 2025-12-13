n = int(input())
list1 = []
for _ in range(n):
    list1.append(list(map(int, input().split())))
s = -float("inf")
while n not in [1, 2]:
    s1 = 0
    s1 += sum(list1[0])
    for i in range(1, n - 1):
        s1 += list1[i][0] + list1[i][-1]
    s1 += sum(list1[-1])
    s = max(s, s1)
    del list1[0]
    for i in range(n - 2):
        del list1[i][0]
        del list1[i][-1]
    del list1[-1]
    n -= 2
if n == 1:
    s = max(s, list1[0][0])
else:
    s1 = sum(list1[0]) + sum(list1[1])
    s = max(s, s1)
print(s)
