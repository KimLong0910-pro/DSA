def binary_search(array, key):
    mid = 0
    left = 0
    right = len(array) - 1
    step = 0

    while left <= right:
        step += 1
        mid = (left + right) // 2

        if key == array[mid]:
            return mid

        if key < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return -1


array = [0, 4, 5, 9, 13, 15, 18, 24, 28, 29, 35]
key = 40
result = binary_search(array, key)
print(f"phan tu tim kiem duoc la: {result}")
