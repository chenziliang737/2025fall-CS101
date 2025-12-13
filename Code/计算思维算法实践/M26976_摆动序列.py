n = int(input())
list1 = list(map(int, input().split()))
list2 = [[0, 0] for _ in range(n)]
list2[0] = [1, 1]
for i in range(1, n):
    a = list1[i]
    for j in range(i):
        b = list1[j]
        if b > a:
            list2[i][0] = max(list2[i][0], list2[j][1] + 1)
        elif b < a:
            list2[i][1] = max(list2[i][1], list2[j][0] + 1)
s = max([max(row) for row in list2])
print(s)
