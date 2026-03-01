class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


l = list(input())
i = 0


def dfs():
    global i
    s = l[i]
    i += 1
    if s != ".":
        node = TreeNode(s)
        node.left = dfs()
        node.right = dfs()
        return node
    else:
        return None


root = dfs()
l1 = []


def dfs1(node):
    if node.left:
        dfs1(node.left)
    l1.append(node.val)
    if node.right:
        dfs1(node.right)


dfs1(root)
print("".join(l1))
l2 = []


def dfs2(node):
    if node.left:
        dfs2(node.left)
    if node.right:
        dfs2(node.right)
    l2.append(node.val)


dfs2(root)
print("".join(l2))
