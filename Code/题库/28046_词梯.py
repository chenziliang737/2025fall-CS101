from collections import deque, defaultdict

n = int(input())
dict1 = defaultdict(list)
for _ in range(n):
    word = input()
    a, b, c, d = list(word)
    e = "_"
    dict1[a + b + c + e].append(word)
    dict1[a + b + e + d].append(word)
    dict1[a + e + c + d].append(word)
    dict1[e + b + c + d].append(word)
start, end = input().split()
dict2 = {start: None}
queue = deque([start])
while queue:
    word = queue.popleft()
    if word == end:
        stack = []
        while word:
            stack.append(word)
            word = dict2[word]
        print(*stack[::-1])
        break
    a, b, c, d = list(word)
    e = "_"
    for t in [a + b + c + e, a + b + e + d, a + e + c + d, e + b + c + d]:
        for child in dict1[t]:
            if child not in dict2:
                queue.append(child)
                dict2[child] = word
else:
    print("NO")
