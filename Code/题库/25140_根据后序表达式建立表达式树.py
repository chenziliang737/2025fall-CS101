from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


for _ in range(int(input())):
    l = input()
    stack = []
    for s in l:
        if ord(s) >= 97:
            stack.append(TreeNode(s))
        else:
            node = TreeNode(s)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    root = stack[-1]
    queue = deque([root])
    ans = []
    while queue:
        node = queue.popleft()
        ans.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print("".join(ans[::-1]))
