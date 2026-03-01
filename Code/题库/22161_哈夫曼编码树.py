import heapq


class TreeNode:
    def __init__(self, name, weight, end=False):
        self.name = name
        self.weight = weight
        self.left = None
        self.right = None
        self.end = end

    def __lt__(self, other):
        if self.weight != other.weight:
            return self.weight < other.weight
        else:
            return self.name[0] < other.name[0]


n = int(input())
heap = []
for _ in range(n):
    s, m = input().split()
    m = int(m)
    heapq.heappush(heap, TreeNode([s], m, True))
while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)
    name = sorted(left.name + right.name)
    weight = left.weight + right.weight
    node = TreeNode(name, weight)
    node.left = left
    node.right = right
    heapq.heappush(heap, node)
root = heap[0]


def encode(root, string):
    res = ""

    def dfs(node, s):
        nonlocal res
        if node.end:
            return
        if s in node.left.name:
            res += "0"
            dfs(node.left, s)
        elif s in node.right.name:
            res += "1"
            dfs(node.right, s)

    for s in string:
        dfs(root, s)
    return res


def decode(root, string):
    n = len(string)
    res = ""

    def dfs(node, i):
        if node.end:
            nonlocal res
            res += node.name[0]
            if i < n:
                dfs(root, i)
            return
        if string[i] == "0":
            dfs(node.left, i + 1)
        else:
            dfs(node.right, i + 1)

    dfs(root, 0)
    return res


while True:
    try:
        string = input()
    except EOFError:
        break
    if string[0].isdigit():
        print(decode(root, string))
    else:
        print(encode(root, string))
