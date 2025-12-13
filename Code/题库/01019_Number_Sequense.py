res = [1]
str1 = ''
for i in range(1, 40000):
    str1 += str(i)
    res.append(res[-1] + len(str1))
t = int(input())
for _ in range(t):
    a = int(input())
    l = 0
    r = len(res)
    while r - l > 1:
        mid = (l + r) // 2
        if res[mid] <= a:
            l = mid
        else:
            r = mid
    print(str1[a - res[l]])
