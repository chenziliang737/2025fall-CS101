from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


l = list(map(int, input().split()))
root = TreeNode(l[0])
for num in l[1:]:
    node = root
    while True:
        mid = node.val
        if num < mid:
            if node.left:
                node = node.left
            else:
                node.left = TreeNode(num)
                break
        elif num > mid:
            if node.right:
                node = node.right
            else:
                node.right = TreeNode(num)
                break
        else:
            break
res = []
queue = deque([root])
while queue:
    node = queue.popleft()
    res.append(node.val)
    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)
print(" ".join(map(str, res)))
