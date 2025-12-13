a = int(input())
b = int(input())
l = max(len(str(a)), len(str(b)))
str1 = str(a).zfill(l)
str2 = str(b).zfill(l)
str3 = ""
e = 0
for i in range(l):
    c = int(str1[l - i - 1])
    d = int(str2[l - i - 1])
    f = c + d + e
    if f >= 10:
        e = 1
        f = f - 10
    else:
        e = 0
    str3 = str(f) + str3
if e == 1:
    str3 = "1" + str3
print(int(str3))
