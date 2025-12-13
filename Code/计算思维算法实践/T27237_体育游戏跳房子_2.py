from collections import deque

while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break

    def calculate(s):
        x = n
        for a in s:
            if a == "H":
                x *= 3
            if a == "O":
                x //= 2
        return x

    queue = deque([""])
    set1 = set([n])
    while queue:
        s = queue.popleft()
        x = calculate(s)
        if x == m:
            print(len(s))
            print(s)
            break
        if x * 3 not in set1:
            queue.append(s + "H")
            set1.add(x * 3)
        if x // 2 not in set1:
            queue.append(s + "O")
            set1.add(x // 2)
