list1 = [0] * 10002
list1[0] = 1
list1[1] = 1
for i in range(2, 101):
    if list1[i] == 0:
        for j in range(2 * i, 10002, i):
            list1[j] = 1
T = int(input())
list2 = []
for _ in range(T):
    a = int(input())
    list2.append(a)
for i in range(len(list2)):
    print(f"Case{i+1}:")
    a = list2[i]
    if a < 12:
        print("NULL")
    else:
        list3 = []
        for j in range(11, a, 10):
            if list1[j] == 0:
                list3.append(str(j))
        print(" ".join(list3).rstrip())
