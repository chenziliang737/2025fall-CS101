p = int(input())
list1 = list(map(int, input().split()))
list1.sort()
l = 0
r = len(list1) - 1
s = 0
while l < r:
    while p >= list1[l]:
        p -= list1[l]
        s += 1
        l += 1
    if l < r:
        if s == 0:
            break
        p += list1[r]
        p -= list1[l]
        r -= 1
        l += 1
    if l == r and p >= list1[l]:
        p -= list1[l]
        s += 1
        l += 1
print(s)
