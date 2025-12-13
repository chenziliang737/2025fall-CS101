n = int(input())
while n != 1:
    if n % 2 == 1:
        m = 3 * n + 1
        print(f'{n}*3+1={m}')
        n = m
    else:
        m = n // 2
        print(f'{n}/2={m}')
        n = m
print('End')
