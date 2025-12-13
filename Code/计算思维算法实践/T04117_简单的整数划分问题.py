list1 = [[0], [0, 1], [0, 1, 1]]
for i in range(3, 51):
    list2 = [0] * (i + 1)
    list2[-1] = 1
    for j in range(i - 1, 0, -1):
        list2[j] = sum(list1[i - j][1 : j + 1])
    list1.append(list2)
while True:
    try:
        N = int(input())
    except EOFError:
        break
    print(sum(list1[N]))
