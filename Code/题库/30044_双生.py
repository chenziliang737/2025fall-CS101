nums = [0] * 66000
p = []
for i in range(2, 66000):
    if nums[i] == 0:
        p.append(i)
    for j in p:
        if i * j >= 66000:
            break
        nums[i * j] = 1
        if i % j == 0:
            break
pset = set(p)


def calculate(i):
    s = bin(i)[2:]
    x = 0
    a = 0
    for j in s:
        if j == '1':
            a += 2 ** x
        x += 1
    return a


x = int(input())
y = -1
for i in p[1:]:
    j = calculate(i)
    if j in pset and j >= i:
        y += 1
        if y == x:
            print(*[i, j])
            break
