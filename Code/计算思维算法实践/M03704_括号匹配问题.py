while True:
    try:
        str1 = input()
    except EOFError:
        break
    stack1 = []
    for i in range(len(str1)):
        if str1[i] == "(":
            stack1.append(i)
        if stack1 and str1[i] == ")":
            del stack1[-1]
    stack2 = []
    for j in range(len(str1) - 1, -1, -1):
        if str1[j] == ")":
            stack2.append(j)
        if stack2 and str1[j] == "(":
            del stack2[-1]
    list1 = [" "] * len(str1)
    for i in stack1:
        list1[i] = "$"
    for j in stack2:
        list1[j] = "?"
    print(str1)
    print("".join(list1))
