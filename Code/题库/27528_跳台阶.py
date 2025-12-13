N = int(input())
dp = [1]
for i in range(N):
    dp.append(sum(dp))
print(dp[-1])
