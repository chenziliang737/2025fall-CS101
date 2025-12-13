n = int(input())
c = 0
w = 0
for i in range(n):
    list1 = list(map(int, input().split()))
    a = list1.count(3)
    if a > w:
        c = i + 1
        w = a
print(c)
