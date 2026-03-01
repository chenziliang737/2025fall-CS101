for _ in range(int(input())):
    expression = input().strip()
    stack1 = []
    s = "0123456789."
    for i in expression:
        if stack1 and i in s and stack1[-1][-1] in s:
            stack1.append(stack1.pop() + i)
        else:
            stack1.append(i)
    priority = {"(": 0, "+": 1, "-": 1, "*": 2, "/": 2}
    stack2 = []
    ans = []
    for i in stack1:
        if i in "+-*/":
            while stack2 and priority[stack2[-1]] >= priority[i]:
                ans.append(stack2.pop())
            stack2.append(i)
        elif i == "(":
            stack2.append(i)
        elif i == ")":
            while stack2[-1] != "(":
                ans.append(stack2.pop())
            stack2.pop()
        else:
            ans.append(i)
    while stack2:
        ans.append(stack2.pop())
    print(" ".join(ans))
