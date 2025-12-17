a=int(input())
def change(a):
    if a//8==0:
        return str(a)
    else:
        return change(a//8)+str(a%8)
print(change(a))
