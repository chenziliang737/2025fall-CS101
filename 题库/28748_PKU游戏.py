n, k = map(int, input().split())
dict1 = {}
dict2 = {}
for i in range(1, n + 1):
    list1 = list(map(int, input().split()))
    for num in list1:
        dict1[num] = i
        dict2[num] = dict2.get(num, 0) + 1
res = [0] * (n + 1)
for num in dict2.keys():
    res[dict1[num]] += dict2[num]
for i in range(1, n + 1):
    print(f'{res[i] / (n * k):.9f}')
