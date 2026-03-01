class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


for _ in range(int(input())):
    tree = list(input())
    stack = []
    for s in tree:
        if s == "(":
            pass
        elif s == "*":
            stack.append(None)
        elif s == ",":
            node = stack.pop()
            stack[-1].left = node
        elif s == ")":
            node = stack.pop()
            stack[-1].right = node
        else:
            stack.append(TreeNode(s))
    root = stack[-1]
    ans1 = []

    def dfs1(node):
        ans1.append(node.val)
        if node.left:
            dfs1(node.left)
        if node.right:
            dfs1(node.right)

    dfs1(root)
    print("".join(ans1))
    ans2 = []

    def dfs2(node):
        if node.left:
            dfs2(node.left)
        ans2.append(node.val)
        if node.right:
            dfs2(node.right)

    dfs2(root)
    print("".join(ans2))
