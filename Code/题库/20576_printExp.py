def priority(op):
    if op == "not":
        return 3
    if op == "and":
        return 2
    if op == "or":
        return 1
    return 0


def is_op(x):
    return x in ("not", "and", "or")


expr = input().strip()
tokens = expr.replace("(", " ( ").replace(")", " ) ").split()

vals, ops = [], []


def apply():
    op = ops.pop()
    if op == "not":
        a, pa = vals.pop()
        if pa < priority(op):
            a = f"( {a} )"
        vals.append((f"not {a}", priority(op)))
    else:
        b, pb = vals.pop()
        a, pa = vals.pop()
        if pa < priority(op):
            a = f"( {a} )"
        if pb <= priority(op):
            b = f"( {b} )"
        vals.append((f"{a} {op} {b}", priority(op)))


for t in tokens:
    if t == "(":
        ops.append(t)
    elif t == ")":
        while ops and ops[-1] != "(":
            apply()
        ops.pop()
    elif is_op(t):
        while (
            ops
            and is_op(ops[-1])
            and (
                (t != "not" and priority(ops[-1]) >= priority(t))
                or (t == "not" and priority(ops[-1]) > priority(t))
            )
        ):
            apply()
        ops.append(t)
    else:
        vals.append((t, 4))

while ops:
    apply()

print(vals[-1][0])
