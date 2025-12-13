from math import ceil, log

p = int(input())
print(ceil(p * log(2, 10)))
a = p // 1000
b = p % 1000
num = 1
for _ in range(a):
    num *= 2**1000
    if len(str(num)) > 500:
        num = int(str(num)[-500:])
for _ in range(b):
    num *= 2
    if len(str(num)) > 500:
        num = int(str(num)[-500:])
a = str(num - 1).zfill(500)
for i in range(10):
    print(a[50 * i : 50 * (i + 1)])
