from collections import defaultdict


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(node):
    if node and node.val != "*":
        return node.val + preorder(node.left) + preorder(node.right)
    else:
        return ""


def inorder(node):
    if node and node.val != "*":
        return inorder(node.left) + node.val + inorder(node.right)
    else:
        return ""


def postorder(node):
    if node and node.val != "*":
        return postorder(node.left) + postorder(node.right) + node.val
    else:
        return ""


ans = []
for _ in range(int(input())):
    level = defaultdict(list)
    condition = defaultdict(int)
    while True:
        s = input()
        if s == "0":
            root = level[0][0]
            ans.append(preorder(root))
            ans.append(postorder(root))
            ans.append(inorder(root))
            ans.append("")
            break
        h = s.count("-")
        v = s[h:]
        node = TreeNode(v)
        if h > 0:
            father = level[h - 1][-1]
            if not father.left:
                father.left = node
            else:
                father.right = node
        level[h].append(node)
ans.pop()
print("\n".join(ans))
