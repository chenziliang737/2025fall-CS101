N = int(input())
for i in range(6, N + 1):
    if N / i == int(N / i):
        print(int(N / i))
        break
