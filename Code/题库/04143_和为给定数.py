from collections import deque
n=int(input())
queue=deque(sorted(list(map(int,input().split()))))
m=int(input())
while len(queue)>=2:
    if queue[0]+queue[-1]==m:
        print(queue[0],queue[-1])
        break
    elif queue[0]+queue[-1]>m:
        queue.pop()
    else:
        queue.popleft()
else:
    print('No')