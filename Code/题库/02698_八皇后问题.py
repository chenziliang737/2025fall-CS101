c = 1
stack = []


def output(c, stack):
    print(f"No. {c}")
    grid = [[0] * 8 for _ in range(8)]
    for i in range(8):
        grid[stack[i]][i] = 1
    for roll in grid:
        print(" ".join(map(str, roll)) + " ")


def dfs(n):
    if n == 8:
        global c
        output(c, stack)
        c += 1
        return
    for i in range(8):
        if stack and any(
            i == stack[j] or abs(n - j) == abs(i - stack[j]) for j in range(n)
        ):
            continue
        else:
            stack.append(i)
            dfs(n + 1)
            stack.pop()


dfs(0)
