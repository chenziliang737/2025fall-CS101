L, N, M = map(int, input().split())
list1 = []
for _ in range(N):
    list1.append(int(input()))


def check(d):
    global list1, L, N, M
    m = 0
    cd = 0
    for i in range(N):
        if L - list1[i] < d:
            m += N - i
            break
        if list1[i] - cd < d:
            m += 1
        else:
            cd = list1[i]
    if m > M:
        return True
    else:
        return False


low = 1
high = L + 1
while low < high:
    mid = (low + high + 1) // 2
    if check(mid):
        high = mid - 1
    else:
        low = mid
print(low)
