import heapq


def combine(A, B):
    A.sort()
    B.sort()
    heap = [(A[0] + B[0], 0, 0)]
    heapq.heapify(heap)
    set1 = set([(0, 0)])
    res = []
    while heapq and len(res) < n:
        s, i, j = heapq.heappop(heap)
        res.append(s)
        if i + 1 < n and (i + 1, j) not in set1:
            heapq.heappush(heap, (A[i + 1] + B[j], i + 1, j))
            set1.add((i + 1, j))
        if j + 1 < n and (i, j + 1) not in set1:
            heapq.heappush(heap, (A[i] + B[j + 1], i, j + 1))
            set1.add((i, j + 1))
    return res


T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(m - 1):
        B = list(map(int, input().split()))
        A = combine(A, B)
    A.sort()
    print(*A)
