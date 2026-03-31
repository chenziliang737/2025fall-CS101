N = int(input())
l = list(map(int, input().split()))
stack = []


def dfs(stack, a):
    if stack and stack[-1] > 0 and a < 0:
        if a + stack[-1] > 0:
            stack[-1] += a
            return
        elif a + stack[-1] == 0:
            stack.pop()
            return
        else:
            a += stack.pop()
            dfs(stack, a)
    else:
        stack.append(a)


for a in l:
    dfs(stack, a)
print(len(stack))
print(*stack)
