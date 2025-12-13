n, w = map(int, input().split())
list1 = []
for _ in range(n):
    vi, wi = map(int, input().split())
    ci = vi / wi
    list1.append((vi, wi, ci))
list1.sort(key=lambda x: -x[2])
s = 0
cw = 0
for i in list1:
    wi = i[1]
    ci = i[2]
    if cw + wi > w:
        s += (w - cw) * ci
        break
    else:
        s += wi * ci
        cw += wi
print(f"{s:.1f}")
