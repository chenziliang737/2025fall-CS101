N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(min([max(abs(i - j) for j in b) for i in a]))
