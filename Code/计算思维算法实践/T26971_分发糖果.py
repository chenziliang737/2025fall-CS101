n = int(input())
score = [float("inf")] + list(map(int, input().split())) + [float("inf")]
candy = [1] * (n + 2)
for i in sorted(range(1, n + 1), key=lambda x: score[x]):
    if score[i - 1] < score[i]:
        candy[i] = max(candy[i], candy[i - 1] + 1)
    if score[i + 1] < score[i]:
        candy[i] = max(candy[i], candy[i + 1] + 1)
print(sum(candy[1:-1]))
