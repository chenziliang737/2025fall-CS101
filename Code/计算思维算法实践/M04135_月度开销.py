N, M = map(int, input().split())
list1 = []
low = 0
high = 0
for _ in range(N):
    a = int(input())
    low = max(low, a)
    high += a
    list1.append(a)


def cost(c):
    global list1
    global M
    global N
    s = 0
    m = 1
    for i in range(N):
        if s + list1[i] > c:
            s = list1[i]
            m += 1
        else:
            s += list1[i]
    if m > M:
        return True
    else:
        return False


while low < high:
    mid = (low + high) // 2
    if cost(mid):
        low = mid + 1
    else:
        high = mid
print(low)
