import sys

data = iter(sys.stdin.read().split("\n"))


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.dir = []
        self.file = []


stack = [TreeNode("ROOT")]
x = 1
ans = []
while True:
    s = next(data)
    if s[0] == "d":
        node = TreeNode(s)
        stack[-1].dir.append(node)
        stack.append(node)
    elif s[0] == "f":
        stack[-1].file.append(s)
    elif s == "]":
        stack.pop()
    elif s == "*":
        stack1 = [stack[-1]]

        def output(s):
            s0 = "|     "
            ans.append((len(stack1) - 1) * s0 + s)

        def dfs(node):
            output(node.val)
            for child in node.dir:
                stack1.append(child)
                dfs(child)
                stack1.pop()
            for file in sorted(node.file):
                output(file)

        ans.append(f"DATA SET {x}:")
        dfs(stack1[-1])
        ans.append("")
        stack = [TreeNode("ROOT")]
        x += 1
    elif s == "#":
        break
print("\n".join(ans[:-1]))
