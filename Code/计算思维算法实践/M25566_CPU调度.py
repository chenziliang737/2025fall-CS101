n = int(input())
list1 = []
for _ in range(n):
    c, w = map(int, input().split())
    list1.append((c, w))
list1.sort(key=lambda x: -x[1])
t_now = 0
t = 0
for tuple in list1:
    t_now += tuple[0]
    t = max(t, t_now + tuple[1])
print(t)
