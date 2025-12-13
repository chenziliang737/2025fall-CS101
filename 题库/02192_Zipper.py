from functools import lru_cache

c = 1
for _ in range(int(input())):
    A, B, C = input().split()
    a = len(A)
    b = len(B)
    A = ' ' + A
    B = ' ' + B
    C = ' ' + C


    @lru_cache(maxsize=None)
    def dfs(i, j):
        if (i, j) == (0, 0):
            return True
        if i > 0 and C[i + j] == A[i] and dfs(i - 1, j):
            return True
        if j > 0 and C[i + j] == B[j] and dfs(i, j - 1):
            return True
        return False


    print(f'Data set {c}: yes') if dfs(a, b) else print(f'Data set {c}: no')
    c += 1
