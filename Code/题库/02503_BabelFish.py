dict1 = {}
while True:
    a = input()
    if a:
        str1, str2 = a.split()
        dict1[str2] = str1
    else:
        break
while True:
    try:
        a = input()
    except EOFError:
        break
    b = dict1.get(a, "eh")
    print(b)
