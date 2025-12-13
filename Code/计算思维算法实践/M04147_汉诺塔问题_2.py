N, a, b, c = input().split()
N = int(N)
stacka = [a]
stackb = [b]
stackc = [c]


def myprint(stack1, stack2):
    num = stack1.pop()
    print(f"{num}:{stack1[0]}->{stack2[0]}")
    stack2.append(num)


def change(stack1, stack2):
    if len(stack1) == 1:
        myprint(stack2, stack1)
    elif len(stack2) == 1:
        myprint(stack1, stack2)
    else:
        a = stack1[-1]
        b = stack2[-1]
        if a > b:
            myprint(stack2, stack1)
        else:
            myprint(stack1, stack2)


for i in range(N, 0, -1):
    stacka.append(i)
if N % 2 == 0:
    while len(stacka) > 1 or len(stackb) > 1:
        change(stacka, stackb)
        if len(stacka) > 1 or len(stackb) > 1:
            change(stacka, stackc)
        if len(stacka) > 1 or len(stackb) > 1:
            change(stackb, stackc)
else:
    while len(stacka) > 1 or len(stackb) > 1:
        change(stacka, stackc)
        if len(stacka) > 1 or len(stackb) > 1:
            change(stacka, stackb)
        if len(stacka) > 1 or len(stackb) > 1:
            change(stackb, stackc)
