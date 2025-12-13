M, N = map(int, input().split())
list1 = [[-1] * (N + 2) for _ in range(M + 2)]
for i in range(1, M + 1):
    list1[i][1 : N + 1] = list(map(int, input().split()))
dict1 = {}
dict2 = {}
for i in range(M * N):
    str1 = input()
    if str1:
        list2 = list(map(int, str1.split()))
        s = sum(list2)
        dict1[i] = list2
        dict2[s] = dict2.get(s, 0) + 1
        dict1[-1] = [-1] * len(list2)
    else:
        dict1[i] = []
        dict2[0] = dict2.get(0, 0) + 1
if all(value == [] for value in dict1.values()):
    dict1[-1] = [-1]


def comparelist(list1, list2):
    T = 1
    if list1 != [] and list2 != []:
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                T = 0
                break
    elif list1 == [] and list2 == []:
        pass
    else:
        T = 0
    return T


a = 0
for i in range(1, M + 1):
    for j in range(1, N + 1):
        answer = dict1[list1[i][j]]
        upanswer = dict1[list1[i - 1][j]]
        downanswer = dict1[list1[i + 1][j]]
        leftanswer = dict1[list1[i][j - 1]]
        rightanswer = dict1[list1[i][j + 1]]
        list3 = [0, 0, 0, 0]
        list3[0] = comparelist(answer, upanswer)
        list3[1] = comparelist(answer, downanswer)
        list3[2] = comparelist(answer, leftanswer)
        list3[3] = comparelist(answer, rightanswer)
        if 1 in list3:
            a += 1
b = 0
c = 0
for key in sorted(dict2.keys()):
    if b > 0.6 * M * N:
        c += dict2[key]
    b += dict2[key]
print(f"{a} {c}")
