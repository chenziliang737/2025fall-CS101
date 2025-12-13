m, n, p = map(int, input().split())
board = []
for _ in range(m):
    board.append(list(map(int, input().split())))


# 0左,1右,2上,3下
def turn(board, direct, m, n):
    if direct == 0:
        return board
    elif direct == 1:
        board1 = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                board1[i][j] = board[m - 1 - i][n - 1 - j]
        return board1
    elif direct == 2:
        board1 = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                board1[n - 1 - j][i] = board[i][j]
        return board1
    elif direct == 3:
        board1 = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                board1[j][m - 1 - i] = board[i][j]
        return board1


def left(board):
    board1 = []
    for row in board:
        stack = []
        set1 = set()
        l = 0
        for i in range(len(row)):
            num = row[i]
            if num == 0:
                continue
            if stack and stack[-1] == num and l not in set1:
                stack.pop()
                stack.append(2 * num)
                set1.add(l)
            else:
                stack.append(num)
                l += 1
        row1 = [0] * len(row)
        row1[:l] = stack
        board1.append(row1)
    return board1


def operate(board, direct):
    if direct == 0:
        return left(board)
    elif direct == 1:
        return turn(left(turn(board, 1, m, n)), 1, m, n)
    else:
        return turn(left(turn(board, direct, m, n)), 5 - direct, n, m)


S = 0


def dfs(board, q):
    if q == p:
        global S
        S = max(S, max([max(row) for row in board]))
        return
    for direct in range(4):
        dfs(operate(board, direct), q + 1)


dfs(board, 0)
print(S)
