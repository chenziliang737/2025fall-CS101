class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def dfs(preorder, inorder):
    if not preorder and not inorder:
        return None
    root = TreeNode(preorder[0])
    i = inorder.index(preorder[0])
    root.left = dfs(preorder[1 : i + 1], inorder[:i])
    root.right = dfs(preorder[i + 1 :], inorder[i + 1 :])
    return root


while True:
    try:
        preorder = list(input())
        inorder = list(input())
    except EOFError:
        break
    root = dfs(preorder, inorder)
    ans = []

    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            ans.append(node.val)

    postorder(root)
    print("".join(ans))
