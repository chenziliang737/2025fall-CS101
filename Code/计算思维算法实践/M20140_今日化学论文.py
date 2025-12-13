from collections import deque

queue = deque()
queue += list(input())
stack = []
while queue:
    a = queue.popleft()
    if a == "]":
        b = stack.pop()
        str1 = ""
        while b != "[":
            str1 = b + str1
            b = stack.pop()
        nstr = ""
        for j in range(len(str1)):
            if str1[j].isdigit():
                nstr += str1[j]
                j += 1
            else:
                str2 = str1[j:]
                break
        n = int(nstr)
        stack += list(str2 * n)
    else:
        stack.append(a)
print("".join(stack))
