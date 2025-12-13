N, a, b, c = input().split()
N = int(N)


def change(N, a, b, c):
    if N == 1:
        print(f"1:{a}->{c}")
    else:
        change(N - 1, a, c, b)
        print(f"{N}:{a}->{c}")
        change(N - 1, b, a, c)


change(N, a, b, c)
