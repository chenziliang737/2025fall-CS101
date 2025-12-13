# 将输入数据延拓为8*7表格，从而统一切换函数
list1 = [[0] * 8 for _ in range(7)]


def switch(list1, i, j):
    list1[i][j] = 1 - list1[i][j]
    list1[i][j - 1] = 1 - list1[i][j - 1]
    list1[i][j + 1] = 1 - list1[i][j + 1]
    list1[i - 1][j] = 1 - list1[i - 1][j]
    list1[i + 1][j] = 1 - list1[i + 1][j]
    return


for i in range(5):
    list1[i + 1][1:7] = list(map(int, input().split()))


# list2实时记录list1改动后的状态，list3记录改动操作
# 枚举第一行的所有可能操作
def result(list1):
    for a in range(64):
        list2 = [[0] * 8 for _ in range(7)]
        list3 = [[0] * 8 for _ in range(7)]
        list2 = [row[:] for row in list1]
        list3[1][1:7] = list(map(int, f"{a:08b}"))[2:8]
        for j in filter(lambda x: list3[1][x] == 1, range(1, 7)):
            switch(list2, 1, j)
        # 对上一行每盏点亮的灯，按下下一行对应的灯，这样可以熄灭1至4行的灯。
        # 如果这时第五行的灯刚好也熄灭，证明最初第一行的操作是正确的。
        for i in range(1, 5):
            for j in range(1, 7):
                if list2[i][j] == 1:
                    list3[i + 1][j] = 1
                    switch(list2, i + 1, j)
        if sum(list2[5][1:7]) == 0:
            return list3


list3 = result(list1)
if list3:
    for i in range(1, 6):
        print(" ".join(map(str, list3[i][1:7])))
