N = int(input())
list1 = list(map(int, input().split()))
list2 = [0] * N
for i in range(N - 1, -1, -1):
    num = list1[i]
    s = 1
    for j in range(i + 1, N):
        if list1[j] > list1[i]:
            s = max(s, 1 + list2[j])
    list2[i] = s
print(max(list2))
