from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.child = []


class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


n = int(input())
l = deque(input().split())


def dfs1():
    s = l.popleft()
    if s[0] == "$":
        return None
    node = BinaryTreeNode(s[0])
    if s[1] == "1":
        return node
    node.left = dfs1()
    node.right = dfs1()
    return node


root1 = dfs1()


def dfs2(node):
    new = TreeNode(node.val)
    childs = node.left
    l = []
    while childs:
        l.append(childs)
        childs = childs.right
    for childs in l:
        new.child.append(dfs2(childs))
    return new


root2 = dfs2(root1)


def dfs3(node):
    new = TreeNode(node.val)
    l = node.child[::-1]
    for childs in l:
        new.child.append(dfs3(childs))
    return new


root3 = dfs3(root2)


def bfs(root):
    ans = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        ans.append(node.val)
        for childs in node.child:
            queue.append(childs)
    return ans


print(*bfs(root3))
