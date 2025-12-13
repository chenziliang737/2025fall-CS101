dict1 = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
}
list1 = list(input().split())
S = 0
s = 0
m = 0
sign = 1
for i in list1:
    if i == "negative":
        sign = -1
    elif i == "million":
        S += (s + m) * 10**6
        s = 0
        m = 0
    elif i == "thousand":
        S += (s + m) * 10**3
        s = 0
        m = 0
    elif i == "hundred":
        s += m * 10**2
        m = 0
    else:
        m += dict1[i]
S += s + m
S *= sign
print(S)
