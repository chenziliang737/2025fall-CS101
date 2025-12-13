set1 = {"+", "-", "*", "/"}


def calculate(i, a, b):
    if i == "+":
        return a + b
    elif i == "-":
        return a - b
    elif i == "*":
        return a * b
    elif i == "/":
        return a / b


list1 = list(input().split())
for i in range(len(list1)):
    if list1[i] not in set1:
        list1[i] = float(list1[i])
while len(list1) > 1:
    for i in range(len(list1) - 2):
        if list1[i] in set1 and list1[i + 1] not in set1 and list1[i + 2] not in set1:
            a = calculate(list1[i], list1[i + 1], list1[i + 2])
            list1[i : i + 3] = [a]
            break
print(f"{list1[0]:.6f}")
