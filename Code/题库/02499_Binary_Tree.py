res = []
for c in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    l, r = 0, 0
    while a > 1 or b > 1:
        if a > b:
            l += a // b
            a = a % b
            if b == 1:
                l -= 1
                break
        else:
            r += b // a
            b = b % a
            if a == 1:
                r -= 1
                break
    res.append(f"Scenario #{c}:")
    res.append(f"{l} {r}")
    res.append("")
print("\n".join(res))
