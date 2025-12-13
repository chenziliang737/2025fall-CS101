import math

while True:
    try:
        a, b = map(int, input().split())
    except EOFError:
        break
    if a > b:
        a, b = b, a
    k = b - a
    if a == int(k * (math.sqrt(5) + 1) / 2):
        print(0)
    else:
        print(1)
