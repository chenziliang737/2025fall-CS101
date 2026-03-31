l = [0, 1, 1]
for _ in range(40):
    l.append(l[-3] + l[-2] + l[-1])
print(l[int(input())])
