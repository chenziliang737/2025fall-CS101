def change(p):
    if p == [n - i for i in range(n)]:
        return [i + 1 for i in range(n)]
    for i in range(n - 2, -1, -1):
        if p[i] < p[i + 1]:
            k = 0
            for j in range(i + 1, n - 1):
                if p[j] > p[i] and p[j + 1] < p[i]:
                    k = j
                    break
            else:
                k = n - 1
            p[i], p[k] = p[k], p[i]
            p1 = p[i + 1 :]
            p[i + 1 :] = sorted(p1)
            break
    return p


m = int(input())
for _ in range(m):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 1:
        print(p[0])
    else:
        for i in range(k):
            p = change(p)
        print(*p)
