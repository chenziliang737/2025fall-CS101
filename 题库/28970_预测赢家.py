for _ in range(int(input())):
    data = iter(map(int, input().split()))
    m = next(data)
    nums = []
    for i in range(m):
        nums.append(next(data))
    dp = {}
    for d in range(m):
        for i in range(m - d):
            if d == 0:
                dp[(i, i)] = [nums[i], 0]
                continue
            l = [0, 0]
            a = nums[i] + dp[(i + 1, i + d)][1]
            b = nums[i + d] + dp[(i, i + d - 1)][1]
            if a >= b:
                l[0] = a
                l[1] = dp[(i + 1, i + d)][0]
            else:
                l[0] = b
                l[1] = dp[(i, i + d - 1)][0]
            dp[(i, i + d)] = l
    if dp[(0, m - 1)][0] >= dp[(0, m - 1)][1]:
        print('true')
    else:
        print('false')
