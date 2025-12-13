n = int(input())
list1 = list(input().split())
list2 = list1[:]
for i in range(n):
    flag = False
    for j in range(n - i - 1):
        if int(list2[j + 1] + list2[j]) > int(list2[j] + list2[j + 1]):
            list2[j], list2[j + 1] = list2[j + 1], list2[j]
            flag = True
    if not flag:
        break
list3 = list1[:]
for i in range(n):
    flag = False
    for j in range(n - i - 1):
        if int(list3[j + 1] + list3[j]) < int(list3[j] + list3[j + 1]):
            list3[j], list3[j + 1] = list3[j + 1], list3[j]
            flag = True
    if not flag:
        break
print("".join(list2) + " " + "".join(list3))
