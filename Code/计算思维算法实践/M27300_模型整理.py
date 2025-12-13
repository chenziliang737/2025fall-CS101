from collections import defaultdict

n = int(input())
set1 = set()
dict1 = defaultdict(list)
dict2 = defaultdict(list)
for _ in range(n):
    model, number = input().split("-")
    set1.add(model)
    if number[-1] == "M":
        dict1[model].append(eval(number[:-1]))
    elif number[-1] == "B":
        dict2[model].append(eval(number[:-1]))
for model in sorted(list(set1)):
    list2 = []
    if model in dict1:
        list2 += list(map(lambda x: str(x) + "M", sorted(dict1[model])))
    if model in dict2:
        list2 += list(map(lambda x: str(x) + "B", sorted(dict2[model])))
    str1 = f"{model}: "
    str1 += ", ".join(list2)
    print(str1)
