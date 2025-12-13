T = int(input())
list1 = list(map(int, input().split()))
list1.sort()
N = len(list1)
c = float("inf")
left = 0
right = N - 1
while left < right:
    a = list1[left] + list1[right]
    if a == T:
        c = T
        break
    if abs(T - a) < abs(T - c):
        c = a
    if a < T and a == 2 * T - c:
        c = a
    if a < T:
        left += 1
    if a > T:
        right -= 1
print(c)
