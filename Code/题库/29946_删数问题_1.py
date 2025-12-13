nums = list(map(int, list(input().strip())))
k = int(input())
n = len(nums)
m = n - k
stack = []
c = m
for i in range(n):
    a = nums[i]
    while stack and stack[-1] > a and n - i >= c + 1:
        stack.pop()
        c += 1
    if c > 0:
        stack.append(a)
        c -= 1
print(int(''.join(map(str, stack))))
