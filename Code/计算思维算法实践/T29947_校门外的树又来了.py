L, M = map(int, input().split())
list1 = []
for _ in range(M):
    a, b = map(int, input().split())
    if not list1:
        list1.append([a, b])
        continue
    flag = True
    while flag:
        for t in list1:
            if t[0] <= a and t[1] >= b:
                flag = False
                break
            elif t[1] >= a and t[0] < a:
                list1.remove(t)
                a = t[0]
                break
            elif t[0] <= b and t[1] > b:
                list1.remove(t)
                b = t[1]
                break
            elif t[0] >= a and t[1] <= b:
                list1.remove(t)
                break
        else:
            list1.append([a, b])
            flag = False
s = L + 1
for t in list1:
    s -= t[1] - t[0] + 1
print(s)
