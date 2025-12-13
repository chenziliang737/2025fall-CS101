nums = [0] * 10 ** 6
p = []
for i in range(2, 10 ** 6):
    if nums[i] == 0:
        nums[i] = 1
        p.append(i)
    for j in p:
        if i * j >= 10 ** 6:
            break
        nums[i * j] = 1
        if i % j == 0:
            break
k = int(input())
for x in p:
    if x > k:
        break
    a = 2 ** x - 1
    l = []
    flag = True
    while flag:
        for y in p:
            if a % y == 0:
                l.append(y)
                a = a // y
                break
        else:
            flag = False
    if a != 1:
        l.append(a)
    if len(l) > 1:
        s = ''
        for i in range(len(l) - 1):
            s += f'{l[i]} * '
        s += f'{l[-1]}'
        s += f' = {2 ** x - 1} = ( 2 ^ {x} ) - 1'
