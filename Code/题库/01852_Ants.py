for _ in range(int(input())):
    l, n = map(int, input().split())
    nums = list(map(int, input().split()))
    m = -float('inf')
    M = -float('inf')
    for a in nums:
        b = min(a, l - a)
        c = max(a, l - a)
        m = max(m, b)
        M = max(M, c)
    print(*[m, M])
