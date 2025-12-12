while True:
    try:
        a=input()
    except EOFError:
        break
    def counts(a):
        dict1={}
        for i in a:
            dict1[i]=dict1.get(i,0)+1
        return dict1
    n=len(a)
    dict1=counts(a)
    flag=True
    if n>1:
        for i in range(2,n+1):
            b=str(int(a)*i).zfill(n)
            if dict1!=counts(b):
                flag=False
                break
    if flag:
        print(a+' is cyclic')
    else:
        print(a+' is not cyclic')