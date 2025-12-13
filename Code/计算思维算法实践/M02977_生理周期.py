p, e, i, d = map(int, input().split())
for day in range(p % 23, 30000, 23):
    if (day - e) % 28 == 0 and (day - i) % 33 == 0:
        if day > d:
            print(day - d)
        else:
            print(day + 21252 - d)
        break
