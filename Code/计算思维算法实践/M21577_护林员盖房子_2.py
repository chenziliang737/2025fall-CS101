m, n = map(int, input().split())
A = []
for _ in range(m):
    A.append(list(map(int, input().split())))

# 计算每个位置上方连续0的个数（高度）
height = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if A[i][j] == 0:
            height[i][j] = 1 if i == 0 else height[i - 1][j] + 1
        else:
            height[i][j] = 0

max_area = 0

# 对于每一行，计算柱状图中的最大矩形面积
for i in range(m):
    # 使用单调栈方法
    stack = []
    left = [-1] * n  # 每个柱子左边第一个小于它的柱子索引
    right = [n] * n  # 每个柱子右边第一个小于它的柱子索引

    # 计算left数组
    for j in range(n):
        while stack and height[i][stack[-1]] >= height[i][j]:
            stack.pop()
        left[j] = stack[-1] if stack else -1
        stack.append(j)

    stack = []
    # 计算right数组
    for j in range(n - 1, -1, -1):
        while stack and height[i][stack[-1]] >= height[i][j]:
            stack.pop()
        right[j] = stack[-1] if stack else n
        stack.append(j)

    # 计算当前行的最大矩形面积
    for j in range(n):
        area = height[i][j] * (right[j] - left[j] - 1)
        max_area = max(max_area, area)

print(max_area)
