line = input()
res = ""
for s in line:
    if 65 <= ord(s) <= 90:
        res += chr(ord(s) + 32)
    elif 97 <= ord(s) <= 122:
        res += chr(ord(s) - 32)
    else:
        res += s
print(res)
