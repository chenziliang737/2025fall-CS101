from collections import deque
x=input()
def check(s):
    queue=deque(list(x))
    stack=[]
    for a in s:
        if stack and stack[-1]==a:
            stack.pop()
            continue
        while queue and queue[0]!=a:
            stack.append(queue.popleft())
        if not queue:
            return False
        else:
            queue.popleft()
    if not stack and not queue:
        return True
    else:
        return False
while True:
    try:
        s=input()
    except EOFError:
        break
    print('YES') if check(s) else print('NO')