n=int(input())
pairs=[i[1:-1] for i in input().split()]
distances=[sum(map(int,i.split(','))) for i in pairs]
price=list(map(int,input().split()))
value=[distances[i]/price[i] for i in range(n)]
if n&1:
    mid_value=sorted(value)[n>>1]
    mid_price=sorted(price)[n>>1]
else:
    mid_value=sum(sorted(value)[(n>>1)-1:(n>>1)+1])/2
    mid_price=sum(sorted(price)[(n>>1)-1:(n>>1)+1])/2
ans=0
for i in range(n):
    if value[i]>mid_value and price[i]<mid_price:
        ans+=1
print(ans)