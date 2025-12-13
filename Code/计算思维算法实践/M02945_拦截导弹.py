k = int(input())
list1 = list(map(int, input().split()))
list2 = [0] * k
list2[-1] = 1
for i in range(k - 2, -1, -1):
    list3 = []
    for j in range(i + 1, k):
        if list1[j] <= list1[i]:
            list3.append(list2[j])
    if list3:
        list2[i] = max(list3) + 1
    else:
        list2[i] = 1
print(max(list2))
