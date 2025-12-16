while True:
    n = int(input())
    if n == 0:
        break
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    tau = 0

    def mergesort(l):
        if len(l) == 1:
            return l
        mid = (len(l) + 1) // 2
        left = l[:mid]
        right = l[mid:]
        return merge(mergesort(left), mergesort(right))

    def merge(left, right):
        global tau
        l = len(left)
        r = len(right)
        j = 0
        res = []
        for i in range(l):
            while j < r and left[i] > right[j]:
                res.append(right[j])
                j += 1
            res.append(left[i])
            tau += j
        res += right[j:]
        return res

    mergesort(nums)
    print(tau)
