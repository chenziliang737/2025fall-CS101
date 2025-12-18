n = int(input())
nums = list(map(int, input().split()))
dict1 = {}
for i, num in enumerate(sorted(nums)):
    if num not in dict1:
        dict1[num] = i + 1


def update(i, x):
    while i <= n:
        tree[i] += x
        i += i & -i


def query(i):
    s = 0
    while i > 0:
        s += tree[i]
        i -= i & -i
    return s


tree = [0] * (n + 1)
for i in range(1, n + 1):
    update(i, 1)
tau = 0
for i in range(n - 1, -1, -1):
    num = nums[i]
    idx = dict1[num]
    tau += query(n) - query(idx)
    update(idx, -1)
print(tau)
