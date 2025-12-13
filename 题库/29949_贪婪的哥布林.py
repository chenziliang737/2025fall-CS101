N, M = map(int, input().split())
list1 = []
for _ in range(N):
    v, w = map(int, input().split())
    c = v / w
    list1.append((v, w, c))
list1.sort(key=lambda x: -x[2])
s = 0
m = M
for t in list1:
    if m >= t[1]:
        s += t[0]
        m -= t[1]
    else:
        s += m * t[2]
        break
print(f'{s:.2f}')
