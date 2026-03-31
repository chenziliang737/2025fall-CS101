import sys


class FenwichTree:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def update(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s


def solve():
    data = iter(sys.stdin.read().split())
    n = int(next(data))
    N = n**2
    l = []
    for _ in range(N):
        l.append(int(next(data)))
    x = l.index(0)
    while x + n <= N - 1:
        l[x], l[x + n] = l[x + n], l[x]
        x += n
    while x < N - 1:
        l[x], l[x + 1] = l[x + 1], l[x]
        x += 1
    l.pop()
    tree = FenwichTree(N)
    tau = 0
    for i in l:
        tau += i - 1 - tree.query(i)
        tree.update(i, 1)
    if tau % 2 == 0:
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    solve()
