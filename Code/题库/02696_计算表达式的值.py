dict1 = {"mul": "*", "div": "//", "add": "+", "sub": "-", "mod": "%"}
for _ in range(int(input())):
    a, x, b = input().split()
    print(eval(a + dict1[x] + b))
