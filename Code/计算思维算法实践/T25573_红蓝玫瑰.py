from collections import deque

roses = deque(list(input()))
list1 = deque([[roses.popleft(), 1]])
while roses:
    a = roses.popleft()
    if a == list1[-1][0]:
        list1[-1][1] += 1
    else:
        list1.append([a, 1])
dp = [[0, 0]]
while list1:
    a, l = list1.popleft()
    row = [0, 0]
    if a == "R":
        row[0] = dp[-1][0]
        row[1] = min(dp[-1][1] + l, dp[-1][0] + 1)
    else:
        row[0] = min(dp[-1][0] + l, dp[-1][1] + 1)
        row[1] = dp[-1][1]
    dp.append(row)
print(dp[-1][0])
