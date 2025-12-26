c = 1
res = []
for _ in range(int(input())):
    p, q = map(int, input().split())

    def check(x, y):
        return 0 <= x <= p - 1 and 0 <= y <= q - 1

    def string(x, y):
        return f"{chr(65+y)}{x+1}"

    def neighbour(x, y):
        d = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        l = []
        for dx, dy in d:
            x1 = x + dx
            y1 = y + dy
            if check(x1, y1):
                l.append((x1, y1))
        l.sort(key=lambda t: string(t[0], t[1]))
        return l

    def solve(p, q):
        for q0 in range(q):
            for p0 in range(p):
                condition = [[False] * q for _ in range(p)]
                condition[p0][q0] = True
                stack = [string(p0, q0)]
                s = ""

                def dfs(x, y):
                    nonlocal s
                    if s:
                        return
                    if len(stack) == p * q:
                        s = "".join(stack)
                        return
                    for x1, y1 in neighbour(x, y):
                        if not condition[x1][y1]:
                            condition[x1][y1] = True
                            stack.append(string(x1, y1))
                            dfs(x1, y1)
                            condition[x1][y1] = False
                            stack.pop()

                dfs(p0, q0)
                if s:
                    return s
        return "impossible"

    res.append(f"Scenario #{c}:" + "\n" + solve(p, q) + "\n" * 2)
    c += 1
print("".join(res).rstrip())
