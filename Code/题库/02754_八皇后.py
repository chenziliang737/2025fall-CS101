list1=[]
output=[]
def eightqueen(list1,output):
    if len(list1)==8:
        str1=''
        for i in list1:
            str1+=str(i)
        output.append(int(str1))
    else:
        j=len(list1)+1
        for bj in range(1,9):
            T=True
            for i in range(1,len(list1)+1):
                if bj==list1[i-1] or abs(j-i)==abs(bj-list1[i-1]):
                    T=False
            if T:
                eightqueen(list1+[bj],output)
eightqueen(list1,output)
n=int(input())
list2=[]
for _ in range(n):
    list2.append(int(input()))
for i in list2:
    print(output[i-1])
