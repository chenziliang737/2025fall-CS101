tran = [["IVX", "IVX"], ["IVX", "XLC"], ["IVX", "CDM"], ["I", "M"]]
list1 = list(input())
i = 0
str1 = ""
while list1:
    a = int(list1.pop())
    if a == 4:
        str2 = "IV"
    elif a == 9:
        str2 = "IX"
    else:
        str2 = "V" * (a // 5) + "I" * (a % 5)
    table = str.maketrans(tran[i][0], tran[i][1])
    str2 = str2.translate(table)
    str1 = str2 + str1
    i += 1
print(str1)
