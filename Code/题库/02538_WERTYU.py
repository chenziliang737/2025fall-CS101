keyboard = ["`1234567890-=", "QWERTYUIOP[]\\", "ASDFGHJKL;'", "ZXCVBNM,./"]
mapping = {}
for row in keyboard:
    for i in range(1, len(row)):
        mapping[row[i]] = row[i - 1]
mapping[" "] = " "
while True:
    try:
        line = input()
    except EOFError:
        break
    res = []
    for i in line:
        res.append(mapping[i])
    print("".join(res))
