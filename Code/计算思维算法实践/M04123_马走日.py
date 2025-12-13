T = int(input())
for _ in range(T):
    n, m, x, y = map(int, input().split())
    s = 0
    list1 = [[0] * m for _ in range(n)]
    list1[x][y] = 1

    def check(x, y):
        if 0 <= x <= n - 1 and 0 <= y <= m - 1:
            return True
        else:
            return False

    def move(x, y, dep):
        if dep == n * m:
            global s
            s += 1
            return
        d = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
        for i in range(8):
            x1 = x + d[i][0]
            y1 = y + d[i][1]
            if check(x1, y1) and list1[x1][y1] == 0:
                list1[x1][y1] = 1
                move(x1, y1, dep + 1)
                list1[x1][y1] = 0

    move(x, y, 1)
    print(s)
