a = list(map(int, list(input())))
x = 0
s = 0
while a:
    s += a.pop() * 8**x
    x += 1
print(s)
