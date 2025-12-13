m = 0
while True:
    try:
        a = input()
    except EOFError:
        break
    m += 1
    list1 = []
    while a != '9':
        list1.append(a)
        a = input()
    dict1 = {}
    flag1 = True
    flag2 = True


    def dfs(dict1, a, i):
        global flag1, flag2
        if not flag1:
            return
        if '-1' in dict1:
            flag1 = False
            return
        if i == len(a):
            dict1['-1'] = -1
            return
        if a[i] not in dict1:
            dict1[a[i]] = {}
            flag2 = False
        dfs(dict1[a[i]], a, i + 1)


    for a in list1:
        flag2 = True
        dfs(dict1, a, 0)
        if not flag1:
            break
    if flag1:
        print(f'Set {m} is immediately decodable')
    else:
        print(f'Set {m} is not immediately decodable')
