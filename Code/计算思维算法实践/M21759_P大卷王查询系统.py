from collections import defaultdict

n, x, y = map(int, input().split())
dict1 = defaultdict(lambda: [0, 0])
for _ in range(n):
    l, s, c = input().split()
    c = int(c)
    dict1[s][0] += 1
    dict1[s][1] += c
m = int(input())
for _ in range(m):
    s = input()
    if dict1[s][0] >= x and dict1[s][1] / dict1[s][0] > y:
        print("yes")
    else:
        print("no")
