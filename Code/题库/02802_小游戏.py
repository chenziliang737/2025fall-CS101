from collections import deque

a = 1
while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    grid = [[" "] * (w + 2) for _ in range(h + 2)]
    for i in range(1, h + 1):
        grid[i][1 : w + 1] = list(input())
    print(f"Board #{a}:")
    a += 1
    c = 1
    while True:
        y1, x1, y2, x2 = map(int, input().split())
        if (x1, y1, x2, y2) == (0, 0, 0, 0):
            break
        grid2 = [roll[:] for roll in grid]
        grid2[x2][y2] = " "
        queue = deque([(x1, y1)])
        dict1 = {(x1, y1): 0}
        while queue:
            x, y = queue.popleft()
            if (x, y) == (x2, y2):
                print(f"Pair {c}: {dict1[(x2,y2)]} segments.")
                break
            t = dict1[(x, y)]
            for x3 in range(x + 1, h + 2):
                if grid2[x3][y] == " ":
                    if (x3, y) not in dict1:
                        queue.append((x3, y))
                        dict1[(x3, y)] = t + 1
                else:
                    break
            for x3 in range(x - 1, -1, -1):
                if grid2[x3][y] == " ":
                    if (x3, y) not in dict1:
                        queue.append((x3, y))
                        dict1[(x3, y)] = t + 1
                else:
                    break
            for y3 in range(y + 1, w + 2):
                if grid2[x][y3] == " ":
                    if (x, y3) not in dict1:
                        queue.append((x, y3))
                        dict1[(x, y3)] = t + 1
                else:
                    break
            for y3 in range(y - 1, -1, -1):
                if grid2[x][y3] == " ":
                    if (x, y3) not in dict1:
                        queue.append((x, y3))
                        dict1[(x, y3)] = t + 1
                else:
                    break
        else:
            print(f"Pair {c}: impossible.")
        c += 1
    print()
