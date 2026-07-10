def binary_search(a, x):
    left = 0
    right = len(a) - 1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


a = [1, 3, 5, 7, 9]
x = 7
kqua = binary_search(a, x)

print(kqua)
