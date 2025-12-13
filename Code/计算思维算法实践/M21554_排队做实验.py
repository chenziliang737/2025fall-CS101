n = int(input())
list1 = list(map(int, input().split()))
list2 = []
for i in range(n):
    list2.append((list1[i], i + 1))
list2.sort()
s = 0
list3 = []
for i in range(n):
    t = list2[i]
    list3.append(t[1])
    s += (n - 1 - i) * t[0]
print(*list3)
print(f"{s/n:.2f}")
