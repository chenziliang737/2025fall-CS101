n = int(input())
str1 = input()
list1 = []
for i in range(len(str1) // n):
    list2 = list(str1[n * i:n * (i + 1)])
    if i % 2 == 0:
        list1.append(list2)
    else:
        list1.append(list2[::-1])
list3 = [list(row) for row in zip(*list1)]
str2 = ''
for row in list3:
    str2 += ''.join(row)
print(str2)
