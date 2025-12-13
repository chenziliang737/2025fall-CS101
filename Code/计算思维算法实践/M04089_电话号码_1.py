for _ in range(int(input())):
    n = int(input())
    dict1 = {}
    flag1 = True
    flag2 = True

    def trie(dict1, s, i):
        global flag1, flag2
        if not flag1:
            return
        if "-1" in dict1:
            flag1 = False
            return
        if i == len(s):
            dict1["-1"] = True
            if flag2:
                flag1 = False
            return
        if s[i] not in dict1:
            flag2 = False
            dict1[s[i]] = {}
        trie(dict1[s[i]], s, i + 1)

    for _ in range(n):
        s = input()
        flag2 = True
        trie(dict1, s, 0)
    print("YES") if flag1 else print("NO")
