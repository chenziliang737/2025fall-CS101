from collections import defaultdict

while True:
    N, M = map(int, input().split())
    if (N, M) == (0, 0):
        break
    score = defaultdict(int)
    for _ in range(N):
        rank = list(map(int, input().split()))
        for i in rank:
            score[i] += 1
    score1 = sorted(score.values(), reverse=True)
    second = []
    for i in score.keys():
        if score[i] == score1[1]:
            second.append(i)
    print(*sorted(second))
