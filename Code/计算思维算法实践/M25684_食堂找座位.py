m, c = map(int, input().split())
dict1 = {}
for _ in range(m):
    n, s, d = map(int, input().split())
    for i in range(s, s + d):
        dict1[i] = dict1.get(i, 0) + n
for i in dict1.values():
    if i > c:
        print("N")
        break
else:
    print("Y")
