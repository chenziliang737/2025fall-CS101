from collections import defaultdict

n, m, L = map(int, input().split())
tree = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
list1 = []
list2 = [0] * n


def dls(a, l):
    list1.append(a)
    list2[a] = 1
    if l == L:
        return
    for b in sorted(tree[a]):
        if list2[b] == 0:
            dls(b, l + 1)


a = int(input())
dls(a, 0)
print(" ".join(map(str, list1)))
