from datetime import date

n = int(input())
list1 = []
for i in range(n):
    list1.append(list(map(int, input().split())))
for i in range(n):
    list_i = list1[i]
    date1 = date(2025, list_i[0], list_i[1])
    date2 = date(2025, list_i[3], list_i[4])
    delta = (date2 - date1).days
    print(list_i[2] * 2**delta)
