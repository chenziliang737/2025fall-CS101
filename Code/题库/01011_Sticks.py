import bisect

while True:
    n = int(input())
    if n == 0:
        break
    sticks = list(map(int, input().split()))
    sticks.sort()
    L = sum(sticks)
    M = sticks[-1]
    for k in range(L // M, 1, -1):
        if L % k == 0:
            d = L // k
            condition = [False] * n
            stack = []


            def dfs(m, x, d):
                if m == n:
                    if x == 0:
                        return True
                    else:
                        return False
                if x == 0:
                    for i in range(n - 1, -1, -1):
                        if condition[i] == False:
                            condition[i] = True
                            stack.append(sticks[i])
                            if dfs(m + 1, sticks[i] % d, d):
                                return True
                            condition[i] = False
                            stack.pop()
                            return False
                a = bisect.bisect(sticks, min(d - x, stack[-1]))
                for i in range(a - 1, -1, -1):
                    if condition[i] == False and sticks[i] <= min(d - x, stack[-1]):
                        if i < a - 1 and condition[i + 1] == False and sticks[i + 1] == sticks[i]:
                            continue
                        condition[i] = True
                        stack.append(sticks[i])
                        if dfs(m + 1, (x + sticks[i]) % d, d):
                            return True
                        condition[i] = False
                        stack.pop()
                        if sticks[i] == d - x:
                            return False
                return False


            if dfs(0, 0, d):
                print(d)
                break
    else:
        print(L)
