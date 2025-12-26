N, M = map(int, input().split())
set1 = set(map(int, input().split()))
if len(set1) == N:
    print(N)
else:
    l = []
    for i in range(N):
        if i not in set1:
            l.append(i)
    print(*l)
