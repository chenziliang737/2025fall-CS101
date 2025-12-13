import bisect

day = [0]
coin = [0]
for i in range(1, 10001):
    day.append(i * (i + 1) // 2)
    coin.append(coin[-1] + i ** 2)
while True:
    n = int(input())
    if n == 0:
        break
    i = bisect.bisect(day, n)
    m = coin[i - 1] + i * (n - day[i - 1])
    print(f'{n} {m}')
