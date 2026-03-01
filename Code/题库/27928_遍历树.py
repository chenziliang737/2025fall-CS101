from collections import defaultdict


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.child = []


n = int(input())
dict1 = {}
dict2 = defaultdict(int)
for _ in range(n):
    l = list(map(int, input().split()))
    a = l[0]
    if a in dict1:
        node = dict1[a]
    else:
        node = TreeNode(a)
        dict1[a] = node
        dict2[a] = 1
    for b in l[1:]:
        if b in dict1:
            node.child.append(dict1[b])
            dict2[b] = 0
        else:
            child = TreeNode(b)
            dict1[b] = child
            node.child.append(child)
for c in dict2:
    if dict2[c] == 1:
        root = dict1[c]
        break


def dfs(node):
    l = [node.val]
    for child in node.child:
        l.append(child.val)
    l.sort()
    for a in l:
        if a == node.val:
            print(a)
        else:
            dfs(dict1[a])


dfs(root)
