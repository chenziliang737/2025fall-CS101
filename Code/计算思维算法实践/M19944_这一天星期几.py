n = int(input())
list1 = []
list2 = []
for i in range(n):
    list1.append(input())
dict1 = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
}
for i in list1:
    m = int(i[4:6])
    if m == 1 or m == 2:
        m += 12
        if i[2:4] == "00":
            y = 99
            c = int(i[:2]) - 1
        else:
            y = int(i[2:4]) - 1
            c = int(i[:2])
    else:
        y = int(i[2:4])
        c = int(i[:2])
    d = int(i[6:8])
    w = (y + int(y / 4) + int(c / 4) - 2 * c + int(26 * (m + 1) / 10) + d - 1) % 7
    list2.append(dict1[w])
for i in list2:
    print(i)
