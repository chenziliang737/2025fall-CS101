for _ in range(int(input())):
    n = int(input())
    p = [0] + list(map(int, input().split()))
    s = ''
    for i in range(1, n + 1):
        s += (p[i] - p[i - 1]) * '(' + ')'
    stack = [0]
    w = []
    for i in s:
        if i == '(':
            stack.append(1)
        else:
            a = stack.pop()
            w.append(a)
            stack[-1] += a
    print(*w)
