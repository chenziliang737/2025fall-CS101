list1 = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
dict1 = {
    0: "1",
    1: "0",
    2: "X",
    3: "9",
    4: "8",
    5: "7",
    6: "6",
    7: "5",
    8: "4",
    9: "3",
    10: "2",
}
n = int(input())
for _ in range(n):
    str1 = input()
    list2 = list(map(int, str1[:17]))
    s = sum(map(lambda x, y: x * y, list1, list2))
    if str1[-1] == dict1[s % 11]:
        print("YES")
    else:
        print("NO")
