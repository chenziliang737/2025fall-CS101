M, N = map(int, input().split())
dict1 = {}
for i in range(1, N + 1):
    P, L, X = map(int, input().split())
    if i == 1:
        L0 = L
    l = [P, L, {}]
    for _ in range(X):
        T, V = map(int, input().split())
        l[2][T] = V
    dict1[i] = l
Mstack = [-float('inf')]
mstack = [float('inf')]
condition = [False] * (N + 1)


def dfs(i):
    if condition[i]:
        return float('inf')
    P, L, dict2 = dict1[i]
    M1 = max(Mstack[-1], L)
    m1 = min(mstack[-1], L)
    if M1 - m1 > M:
        return float('inf')
    if not dict2:
        return P
    Mstack.append(M1)
    mstack.append(m1)
    condition[i] = True
    b = P
    for j in dict2:
        b = min(b, dict2[j] + dfs(j))
    Mstack.pop()
    mstack.pop()
    condition[i] = False
    return b


print(dfs(1))
