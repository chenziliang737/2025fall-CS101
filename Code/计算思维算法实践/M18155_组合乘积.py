T = int(input())
list1 = list(map(int, input().split()))
dict1 = {x: 0 for x in list1}
flag = False


def dfs(t):
    if t == 1:
        global flag
        flag = True
        return
    if flag:
        return
    for x in list1:
        if dict1[x] == 0 and t % x == 0:
            dict1[x] = 1
            dfs(t // x)
            dict1[x] = 0


dfs(T)
if flag:
    print("YES")
else:
    print("NO")
