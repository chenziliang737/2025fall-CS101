set1={'+','-','*','/'}
def calculate(i,a,b):
    if i=='+':
        return (a+b)
    elif i=='-':
        return (a-b)
    elif i=='*':
        return (a*b)
    elif i=='/':
        return (a/b)
stack1=list(input().split())
for i in range(len(stack1)):
    if stack1[i] not in set1:
        stack1[i]=float(stack1[i])
stack2=[]
while stack1:
    i=stack1.pop()
    if i in set1:
        a=stack2.pop()
        b=stack2.pop()
        stack2.append(calculate(i,a,b))
    else:
        stack2.append(i)
print(f'{stack2[-1]:.6f}')
