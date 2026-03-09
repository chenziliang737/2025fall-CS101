class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def dfs(po, io):
    if not po or not io:
        return None
    node = TreeNode(po[0])
    i = io.index(po[0])
    node.left = dfs(po[1 : i + 1], io[:i])
    node.right = dfs(po[i + 1 :], io[i + 1 :])
    return node


def post(node):
    if not node:
        return ""
    return post(node.left) + post(node.right) + node.val


while True:
    try:
        po, io = input().split()
    except EOFError:
        break
    print(post(dfs(po, io)))
