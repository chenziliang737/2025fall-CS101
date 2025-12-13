"""
首先l<=a,b<=r
若a不在[b-x,b+x]内，一步
1.l<=b-x<b<b+x<=r
若a在[b-x,b+x]内，两步
2.l<=b-x<b<=r<b+x
若l+x<=a<=r,两步
若b-x<a<l+x:
    若r-a>=x,三步
    若r-a<x,-1
3.b-x<l<=b<b+x<=r
若l<=a<=r-x,两步
若r-x<a<b+x:
    若a-l>=x,三步
    若a-l<=x,-1
4.b-x<l<=b<=r<b+x
-1
等价于：
若a<=b-x or a>=b+x,一步
若(abs(l-a)>=x and abs(l-b)>=x) or (abs(r-a)>=x and abs(r-b)>=x),两步
若(abs(r-a)>=x and abs(l-b)>=x) or (abs(l-a)>=x and abs(r-b)>=x),三步
其余-1
"""

t = int(input())
for _ in range(t):
    l, r, x = map(int, input().split())
    a, b = map(int, input().split())
    if a == b:
        print(0)
    elif abs(b - a) >= x:
        print(1)
    elif any(all(abs(i - j) >= x for j in [a, b]) for i in [l, r]):
        print(2)
    elif any(all(abs([l, r][j] - [a, b][j - i]) >= x for j in [0, 1]) for i in [0, 1]):
        print(3)
    else:
        print(-1)
