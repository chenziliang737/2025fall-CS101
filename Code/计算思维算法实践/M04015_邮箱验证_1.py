while True:
    try:
        str1 = input()
    except EOFError:
        break
    T = True
    if str1.count("@") != 1:
        T = False
    if str1[0] in "@." or str1[-1] in "@.":
        T = False
    if T:
        str2 = str1.split("@")
        if str2[1].count(".") < 1:
            T = False
        if str2[0][-1] == ".":
            T = False
        if str2[1][0] == ".":
            T = False
    if T:
        print("YES")
    if not T:
        print("NO")
