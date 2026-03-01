import heapq


class TreeNode:
    def __init__(self, weight=0):
        self.weight = weight
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.weight < other.weight


n = int(input())
l = list(map(int, input().split()))
heap = []
for num in l:
    heapq.heappush(heap, (num, TreeNode(num)))
while len(heap) > 1:
    a, left = heapq.heappop(heap)
    b, right = heapq.heappop(heap)
    node = TreeNode()
    node.left = left
    node.right = right
    heapq.heappush(heap, (a + b, node))
root = heap[0][1]


def dfs(node, depth):
    if not node:
        return 0
    return node.weight * depth + dfs(node.left, depth + 1) + dfs(node.right, depth + 1)


print(dfs(root, 0))
