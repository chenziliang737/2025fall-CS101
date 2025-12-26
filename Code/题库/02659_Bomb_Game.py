A, B, K = map(int, input().split())
bomb = []
for _ in range(K):
    bomb.append(tuple(map(int, input().split())))
bomb.sort(key=lambda x: (-x[3], x[2]))
R0, S0, P0, T0 = bomb[0]
dict1 = {}
for i in range(1, A + 1):
    for j in range(1, B + 1):
        if abs(R0 - i) <= (P0 - 1) // 2 and abs(S0 - j) <= (P0 - 1) // 2:
            dict1[(i, j)] = 1
for t in bomb[1:]:
    R, S, P, T = t
    l = []
    for x, y in dict1.keys():
        if abs(R - x) <= (P - 1) // 2 and abs(S - y) <= (P - 1) // 2 and T == 0:
            l.append((x, y))
        if (abs(R - x) > (P - 1) // 2 or abs(S - y) > (P - 1) // 2) and T == 1:
            l.append((x, y))
    for x, y in l:
        dict1.pop((x, y))
print(len(dict1))
