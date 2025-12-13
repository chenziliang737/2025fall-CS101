dict1 = {chr(i): i - 97 for i in range(97, 123)}
str1 = input()
n = len(str1)
list1 = [dict1[str1[i]] for i in range(n)]


def change(list1):
    i = n - 1
    while list1[i] == 25:
        list1[i] = 0
        i -= 1
    else:
        list1[i] += 1


k = int(input())
for _ in range(k + 1):
    change(list1)
str2 = ""
for i in list1:
    str2 += chr(97 + i)
print(str2)
