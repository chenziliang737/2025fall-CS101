while True:
    n = int(input())
    if n == 0:
        break
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    list1.sort()
    list2.sort()
    s = 0
    while list2:
        if list2[-1] > list1[-1]:
            list2.pop()
            del list1[0]
            s -= 200
        elif list2[-1] < list1[-1]:
            list2.pop()
            list1.pop()
            s += 200
        elif list2[-1] == list1[-1]:
            if list2[0] < list1[0]:
                del list2[0]
                del list1[0]
                s += 200
            else:
                if list1[0] < list2[-1]:
                    s -= 200
                list2.pop()
                del list1[0]
    print(s)
