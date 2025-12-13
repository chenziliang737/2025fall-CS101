def change(p):
    if p == [N - i for i in range(N)]:
        return [i + 1 for i in range(N)]
    for i in range(N - 2, -1, -1):
        if p[i] < p[i + 1]:
            k = 0
            for j in range(i + 1, N - 1):
                if p[j] > p[i] and p[j + 1] < p[i]:
                    k = j
                    break
            else:
                k = N - 1
            p[i], p[k] = p[k], p[i]
            p1 = p[i + 1 :]
            p[i + 1 :] = sorted(p1)
            break
    return p


N = int(input())
M = int(input())
p = list(map(int, input().split()))
for _ in range(M):
    p = change(p)
print(*p)
