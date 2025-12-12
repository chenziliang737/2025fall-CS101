l0=list(input())
def decode(l):
    n=len(l)
    if n<=2:
        return l
    a=l[0]
    l1=l[1:(n+1)//2]
    l2=l[(n+1)//2:]
    return decode(l1)+[a]+decode(l2)
print(''.join(decode(l0)))