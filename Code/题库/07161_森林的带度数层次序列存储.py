from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.child = []


n = int(input())
ans = []
for _ in range(n):
    l = deque(input().split())
    queue = deque()
    s = l.popleft()
    m = int(l.popleft())
    root = TreeNode(s)
    if m > 0:
        queue.append([root, m])
    while l:
        s = l.popleft()
        m = int(l.popleft())
        node = TreeNode(s)
        if queue:
            queue[0][0].child.append(node)
            queue[0][1] -= 1
            if queue[0][1] == 0:
                queue.popleft()
        if m > 0:
            queue.append([node, m])

    def postorder(node):
        for child in node.child:
            postorder(child)
        ans.append(node.val)

    postorder(root)
print(" ".join(ans))
