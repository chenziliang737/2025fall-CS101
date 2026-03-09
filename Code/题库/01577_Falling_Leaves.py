from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.val < other.val


def solve(tree):
    root = TreeNode(tree.pop())
    queue = deque([root])
    while tree:
        roll = deque([TreeNode(x) for x in tree.pop()])
        for _ in range(len(queue)):
            if roll and roll[0] < queue[0]:
                node = roll.popleft()
                if not queue[0].left:
                    queue[0].left = node
                elif not queue[-1].right:
                    queue[-1].right = node
                queue.append(node)
            queue.append(queue.popleft())
        if roll:
            node = roll.popleft()
            queue[-1].right = node
            queue.append(node)

    def preorder(node):
        if node:
            return node.val + preorder(node.left) + preorder(node.right)
        else:
            return ""

    print(preorder(root))


tree = []
while True:
    s = input()
    if s in ["*", "$"]:
        solve(tree)
        tree = []
        if s == "$":
            break
    else:
        tree.append(s)
