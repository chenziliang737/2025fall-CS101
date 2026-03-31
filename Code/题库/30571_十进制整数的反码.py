N = int(input())
x = len(bin(N)) - 2
a = (1 << x) - 1
print(N ^ a)
