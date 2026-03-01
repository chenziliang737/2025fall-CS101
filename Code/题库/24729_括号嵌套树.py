class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.child = []


tree = list(input())
stack = []
for s in tree:
    if s == "(":
        pass
    elif s in [",", ")"]:
        node = stack.pop()
        stack[-1].child.append(node)
    else:
        stack.append(TreeNode(s))
root = stack[-1]
s1 = ""


def dfs1(node):
    global s1
    s1 += node.val
    for child in node.child:
        dfs1(child)


dfs1(root)
print(s1)
s2 = ""


def dfs2(node):
    global s2
    for child in node.child:
        dfs2(child)
    s2 += node.val


dfs2(root)
print(s2)
