n=int(input())
dict1={}
str1='abcdefghijklmnoprstuvwxy'
str2='222333444555666777888999'
table=str.maketrans(str1,str2)
for _ in range(n):
    s=input().lower().replace('-','')
    s=s.translate(table)
    s=s[:3]+'-'+s[3:]
    dict1[s]=dict1.get(s,0)+1
T=True
for key in sorted(dict1):
    if dict1[key]>1:
        print(key,dict1[key])
        T=False
if T:
    print("No duplicates.")