from math import ceil

power = [-1] + list(map(int, input().split()))
power.sort()
large_num = 10 ** 12
power.append(large_num)
n = len(power)
for i in range(n):
    swap = False
    for j in range(1, n - i):
        for k in range(n - i - j - 1, 0, -1):
            if ceil(power[j] / j) + ceil(power[j + k] / (j + k)) > ceil(power[j + k] / j) + ceil(power[j] / (j + k)):
                power[j], power[j + k] = power[j + k], power[j]
                swap = True
    if not swap:
        break
print(sum(map(lambda x: ceil(power[x] / x), range(1, n - 1))))
