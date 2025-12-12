from math import log,ceil
from decimal import Decimal
while True:
    try:
        line=input()
    except EOFError:
        break
    R=Decimal(line.split()[0])
    n=int(line.split()[1])
    m=ceil(log(10000/R,10))
    R_1=int(R*10**m)
    list1=list(str(R_1**n))
    stack=[]
    for _ in range(m*n):
        if not list1:
            stack.append('0')
            continue
        a=list1.pop()
        if not stack and a=='0':
            continue
        stack.append(a)
    print(''.join(list1)+'.'+''.join(stack[::-1])) if stack else print(''.join(list1))