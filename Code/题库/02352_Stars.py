class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        i = index
        while i <= self.size:
            self.tree[i] += delta
            i += i & -i

    def query(self, index):
        res = 0
        i = index
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res


N = int(input())
tree = FenwickTree(32005)
level = [0] * N
for _ in range(N):
    x, y = map(int, input().split())
    level[tree.query(x + 1)] += 1
    tree.update(x + 1, 1)
for l in level:
    print(l)
