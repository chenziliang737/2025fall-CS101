def mycount(a, s):
    # mycount(a,s)函数计算的是a的分解中第一项大于等于s的部分
    # 计算原理：将a的分解项拆分为a的第一项i和其余所有项（即a//i的分解项）
    # 固定a和i，令其余所有项即a//i的分解项任意变化，这样得到的排列数等于mycount(a//i,i)
    # 令i遍历所有小于等于sqrt(a)的数，各项排列数之和就是a的分解种数
    # 但要注意的是，a//i的分解项中的每个数都必须大于等于i，否则该项会重复计算
    # 因此计算分解种数时需要引入两个参数a和s，使i的取值从s开始
    # 最后的待求量即为mycount(a,2)
    c = 0
    for i in range(s, int(a**0.5 + 1)):
        if a % i == 0 and i <= a // i:
            c += mycount(a // i, i)
    # 由于i总是小于等于sqrt(a)，上面的计算会漏掉a=a项，故令c再加一
    # 循环体中的i<=a//i保证了a>=s
    # 有两种情况会使上面的循环体不进行，也即基线条件：
    # 一是a==s，此时最初的展开式末两项相同（例如16=4*4），不能再进行拆分，故c=1
    # 另一是a>s，且a与s互质，此时a也只能直接乘在分解项的最后面，故c=1
    # 综上所述，只需一行c+=1就能覆盖包括基线条件和递归条件在内的所有情况
    c += 1
    return c


n = int(input())
list1 = []
for _ in range(n):
    a = int(input())
    list1.append(mycount(a, 2))
for a in list1:
    print(a)
