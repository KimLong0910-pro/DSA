def reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def rotateRight(arr, k):
    n = len(arr)
    k %= n

    reverse(arr, 0, n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)


arr = [1, 2, 3, 4, 5]
rotateRight(arr, 2)
print(arr)
