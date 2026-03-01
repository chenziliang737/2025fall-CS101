class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def dfs(inorder, postorder):
    if not inorder and not postorder:
        return None
    root = TreeNode(postorder[-1])
    i = inorder.index(postorder[-1])
    root.left = dfs(inorder[:i], postorder[:i])
    root.right = dfs(inorder[i + 1 :], postorder[i:-1])
    return root


def preorder(node):
    if not node:
        return ""
    return node.val + preorder(node.left) + preorder(node.right)


inorder = list(input())
postorder = list(input())
root = dfs(inorder, postorder)
print(preorder(root))
