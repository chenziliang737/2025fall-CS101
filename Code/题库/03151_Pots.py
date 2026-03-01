from collections import deque

A, B, C = map(int, input().split())
queue = deque([(0, 0)])
dict1 = {(0, 0): []}
while queue:
    a, b = queue.popleft()
    l = dict1[(a, b)]
    if C in [a, b]:
        print(len(l))
        for s in l:
            print(s)
        break
    if (A, b) not in dict1:
        queue.append((A, b))
        dict1[(A, b)] = l + ["FILL(1)"]
    if (a, B) not in dict1:
        queue.append((a, B))
        dict1[(a, B)] = l + ["FILL(2)"]
    if (0, b) not in dict1:
        queue.append((0, b))
        dict1[(0, b)] = l + ["DROP(1)"]
    if (a, 0) not in dict1:
        queue.append((a, 0))
        dict1[(a, 0)] = l + ["DROP(2)"]
    if a + b < A and (a + b, 0) not in dict1:
        queue.append((a + b, 0))
        dict1[(a + b, 0)] = l + ["POUR(2,1)"]
    if a + b > A and (A, a + b - A) not in dict1:
        queue.append((A, a + b - A))
        dict1[(A, a + b - A)] = l + ["POUR(2,1)"]
    if a + b < B and (0, a + b) not in dict1:
        queue.append((0, a + b))
        dict1[(0, a + b)] = l + ["POUR(1,2)"]
    if a + b > B and (a + b - B, B) not in dict1:
        queue.append((a + b - B, B))
        dict1[(a + b - B, B)] = l + ["POUR(1,2)"]
else:
    print("impossible")
