import math

n = int(input())
for i in range(1, n + 1):
    x, y = map(float, input().split())
    S = math.pi * (pow(x, 2) + pow(y, 2))
    Z = int(S / 100) + 1
    print(f'Property {i}: This property will begin eroding in year {Z}.')
print('END OF OUTPUT.')
