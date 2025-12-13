T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    list1 = [["."] * (M + 2) for _ in range(N + 2)]
    for i in range(1, N + 1):
        list1[i][1:-1] = list(input())
    s = 0
    S = 0

    def dfs(x, y):
        global s
        if list1[x][y] == ".":
            return
        list1[x][y] = "."
        s += 1
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                dfs(x + dx, y + dy)

    for x in range(1, N + 1):
        for y in range(1, M + 1):
            if list1[x][y] == "W":
                s = 0
                dfs(x, y)
                S = max(S, s)
    print(S)
