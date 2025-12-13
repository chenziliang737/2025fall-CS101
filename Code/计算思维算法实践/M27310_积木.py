from collections import defaultdict

N = int(input())
dict1 = defaultdict(list)
for i in range(1, 5):
    str1 = input()
    for w in set(str1):
        dict1[w].append(i)
flag = False


def dfs(la, lb):
    if not la:
        global flag
        flag = True
        return
    w = la[0]
    for i in dict1[w]:
        if i not in lb:
            lb.append(i)
            dfs(la[1:], lb)
            lb.remove(i)


for _ in range(N):
    la = list(input())
    flag = False
    dfs(la, [])
    if flag:
        print("YES")
    else:
        print("NO")
