n = int(input())
s = 0
for x in range(1, n + 1):
    if x % 7 != 0 and "7" not in str(x):
        s += x**2
print(s)
