str1 = input()
if str1.isdigit():
    tran = [["IVX", "IVX"], ["IVX", "XLC"], ["IVX", "CDM"], ["I", "M"]]
    list1 = list(str1)
    i = 0
    str2 = ""
    while list1:
        a = int(list1.pop())
        if a == 4:
            str3 = "IV"
        elif a == 9:
            str3 = "IX"
        else:
            str3 = "V" * (a // 5) + "I" * (a % 5)
        table = str.maketrans(tran[i][0], tran[i][1])
        str3 = str3.translate(table)
        str2 = str3 + str2
        i += 1
    print(str2)
else:
    sign = {"I": 1, "V": 1, "X": 1, "L": 1, "C": 1, "D": 1, "M": 1}
    value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    list1 = list(str1)
    s = 0
    while list1:
        a = list1.pop()
        s += sign[a] * value[a]
        if a == "V" or a == "X":
            sign["I"] = -1
        if a == "L" or a == "C":
            sign["X"] = -1
        if a == "D" or a == "M":
            sign["C"] = -1
    print(s)
