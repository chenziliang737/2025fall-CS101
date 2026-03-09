import sys

sys.setrecursionlimit(1 << 20)
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.dp1 = -1
        self.dp2 = -1
        self.dp = -1


N = int(input())
value = list(map(int, input().split()))
root = TreeNode(value[0])
queue = deque([root])
for v in value[1:]:
    node = TreeNode(v)
    if not queue[0].left:
        queue[0].left = node
    else:
        queue[0].right = node
        queue.popleft()
    queue.append(node)


def dfs(node):
    if not node.left and not node.right:
        node.dp1 = node.val
        node.dp2 = 0
        node.dp = node.val
        return
    elif node.left and node.right:
        if node.left.dp == -1:
            dfs(node.left)
        if node.right.dp == -1:
            dfs(node.right)
        node.dp1 = node.val + node.left.dp2 + node.right.dp2
        node.dp2 = node.left.dp + node.right.dp
        node.dp = max(node.dp1, node.dp2)
        return
    else:
        if node.left:
            child = node.left
        if node.right:
            child = node.right
        if child.dp == -1:
            dfs(child)
        node.dp1 = node.val + child.dp2
        node.dp2 = child.dp
        node.dp = max(node.dp1, node.dp2)
        return


dfs(root)
print(root.dp)
