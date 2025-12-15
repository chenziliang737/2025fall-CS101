key = input()
message = input()
l = []
for s in message:
    if s == " ":
        l.append(s)
    elif s.isupper():
        t = s.lower()
        l.append(key[ord(t) - 97].upper())
    else:
        l.append(key[ord(s) - 97])
print("".join(l))
