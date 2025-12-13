while True:
    try:
        str1 = input()
    except EOFError:
        break
    stra, strb = str1.split()
    a = len(stra)
    b = len(strb)
    stra = "0" + stra
    strb = "0" + strb
    list1 = [[0] * (b + 1) for _ in range(a + 1)]
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if stra[i] == strb[j]:
                list1[i][j] = 1 + list1[i - 1][j - 1]
            else:
                list1[i][j] = max(list1[i - 1][j], list1[i][j - 1])
    print(list1[-1][-1])
