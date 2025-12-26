for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    S = 0
    for i in range(n - 1):
        S += abs(nums[i + 1] - nums[i])
    a = max(abs(nums[1] - nums[0]), abs(nums[-2] - nums[-1]))
    for i in range(1, n - 1):
        b = (
            abs(nums[i] - nums[i - 1])
            + abs(nums[i + 1] - nums[i])
            - abs(nums[i + 1] - nums[i - 1])
        )
        a = max(a, b)
    print(S - a)
