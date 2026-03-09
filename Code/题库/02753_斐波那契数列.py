def fb(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return fb(x - 1) + fb(x - 2)


n = int(input())
list1 = []
for _ in range(n):
    a = int(input())
    list1.append(fb(a))
for i in list1:
    print(i)
