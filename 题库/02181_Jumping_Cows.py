P=int(input())
potion=[]
for _ in range(P):
    potion.append(int(input()))
dp1=[potion[0]]
dp2=[0]
for x in potion[1:]:
    a=max(dp1[-1],dp2[-1]+x)
    b=max(dp2[-1],dp1[-1]-x)
    dp1.append(a)
    dp2.append(b)
print(max(dp1[-1],dp2[-1]))