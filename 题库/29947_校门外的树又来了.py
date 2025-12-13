L, M = map(int, input().split())
list1 = []
for _ in range(M):
    list1.append(list(map(int, input().split())))
list1.sort()
stack = []
for t in list1:
    if stack and t[0] <= stack[-1][1]:
        stack[-1][1] = max(stack[-1][1], t[1])
    else:
        stack.append(t)
print(L + 1 - sum(map(lambda x: x[1] - x[0] + 1, stack)))
