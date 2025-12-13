list1 = list(input())
n = len(list1)
if n == 1:
    print(list1[0])
else:
    list2 = [i for i in range(n)]
    list3 = [(n - 1 - i) for i in range(n)]
    while True:
        str1 = ""
        for k in list2:
            str1 += list1[k]
        print(str1)
        for i in range(n - 1, 0, -1):
            if list2[i - 1] < list2[i]:
                min = float("inf")
                min_index = -1
                for j in range(i, n, 1):
                    if list2[i - 1] < list2[j] < min:
                        min = list2[j]
                        min_index = j
                a = list2[i - 1]
                b = list2[min_index]
                list2[i - 1] = b
                list2[min_index] = a
                list2[i:] = sorted(list2[i:])
                break
        if list2 == list3:
            break
    str1 = ""
    for k in list2:
        str1 += list1[k]
    print(str1)
