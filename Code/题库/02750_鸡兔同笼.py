a = int(input())
if a % 2 != 0:
    print("0 0")
elif a % 4 == 0:
    print(f"{a//4} {a//2}")
else:
    print(f"{a//4+1} {a//2}")
