n = int(input())
arr = list(map(int, input().split()))
tau = 0


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return combine(left, right)


def combine(left, right):
    left += [200000]
    right += [float("inf")]
    list1 = []
    i = j = 0
    c = 0
    while i < len(left) - 1 or j < len(right) - 1:
        if left[i] > right[j]:
            list1.append(right[j])
            j += 1
        else:
            list1.append(left[i])
            i += 1
            c += j
    global tau
    tau += c
    return list1


merge_sort(arr)
print(tau)
