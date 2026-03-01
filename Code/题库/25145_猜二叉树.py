from collections import deque


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


for _ in range(int(input())):
    inorder = list(input())
    postorder = list(input())
    root = dfs(inorder, postorder)
    queue = deque([root])
    l = []
    while queue:
        node = queue.popleft()
        l.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print("".join(l))
