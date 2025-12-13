n = int(input())
pairs = [i[1:-1] for i in input().split()]
distances = list([sum(map(int, i.split(","))) for i in pairs])
prices = list(map(int, input().split()))
ce = [distances[i] / prices[i] for i in range(len(prices))]


def central_number(list1):
    x = len(list1)
    list2 = sorted(list1)
    if x % 2 == 0:
        y = (list2[x // 2 - 1] + list2[x // 2]) / 2
    else:
        y = list2[(x - 1) // 2]
    return y


a = central_number(ce)
b = central_number(prices)
s = 0
for i in range(len(prices)):
    if ce[i] > a and prices[i] < b:
        s += 1
print(s)
