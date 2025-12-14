N, d = map(int, input().split())
position = [(0, 0)]
connection = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    x, y = map(int, input().split())
    position.append((x, y))
    for j in range(1, i + 1):
        x1, y1 = position[j]
        if (x - x1) ** 2 + (y - y1) ** 2 <= d**2:
            connection[i][j] = 1
            connection[j][i] = 1
p = [i for i in range(N + 1)]
condition = [False] * (N + 1)


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


while True:
    try:
        line = input().split()
    except EOFError:
        break
    if line[0] == "O":
        x = int(line[1])
        condition[x] = True
        for y in range(1, N + 1):
            if condition[y] and connection[x][y]:
                p[find(y)] = x
    elif line[0] == "S":
        x, y = int(line[1]), int(line[2])
        if not condition[x] or not condition[y]:
            print("FAIL")
            continue
        if find(x) == find(y):
            print("SUCCESS")
        else:
            print("FAIL")
