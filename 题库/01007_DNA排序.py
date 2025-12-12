from collections import defaultdict
n,m=map(int,input().split())
list1=[]
for _ in range(m):
    list1.append(input())
def calculate(str1):
    dict1=defaultdict(int)
    dict2={'A':1,'C':2,'G':3,'T':4}
    tau=0
    for a in str1[::-1]:
        tau+=sum([dict1[i] for i in range(dict2[a])])
        dict1[dict2[a]]+=1
    return tau
list1.sort(key=calculate)
for a in list1:
    print(a)