list1 = list(input().split())
i = -1


def exp():
    global list1
    global i
    i += 1
    str = list1[i]
    if str == "+":
        return exp() + exp()
    elif str == "-":
        return exp() - exp()
    elif str == "*":
        return exp() * exp()
    elif str == "/":
        return exp() / exp()
    else:
        return float(str)


s = exp()
print(f"{s:.6f}")
