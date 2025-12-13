prime = [0 for i in range(10**4 + 1)]
common = []
for i in range(2, 10**4 + 1):
    if prime[i] == 0:
        common.append(i)
    for j in common:
        if i * j > 10**4:
            break
        prime[i * j] = 1
        if i % j == 0:
            break
tprime = {x**2 for x in common}
m, n = map(int, input().split())
for _ in range(m):
    list1 = list(map(int, input().split()))
    s = 0
    n = 0
    for i in list1:
        if i in tprime:
            s += i
        n += 1
    if s == 0:
        print(0)
    else:
        print(f"{s/n:.2f}")
