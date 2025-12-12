'''
由题意得
1/a=(1/b+1/c)(1-1/b*1/c)=(b+c)/(b*c-1)
a*(b+c)=b*c-1
两边加上a**2得
a**2-a*(b+c)+b*c=a**2+1
a**2+1=(b-a)*(c-a)
只要找到a**2+1的因数中小于math.sqrt(a**2+1)的最大的数即可。
'''
import math
a=int(input())
m=a**2+1
for x in range(int(math.sqrt(m)),0,-1):
    if m%x==0:
        print(x+m//x+2*a)
        break