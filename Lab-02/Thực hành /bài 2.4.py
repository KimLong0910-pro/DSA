def binary_search(arr, left, right, key):
    if right >= left:
        mid = (left + right) // 2

        if arr[mid] == key:
            return mid

        elif arr[mid] > key:
            return binary_search(arr, left, mid - 1, key)

        else:
            return binary_search(arr, mid + 1, right, key)

    else:
        return -1


arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

key1 = 95
kqua1 = binary_search(arr, 0, len(arr) - 1, key1)

if kqua1 != -1:
    print(f"vi tri tim thay {key1} la: {str(kqua1)}")
else:
    print(f"khong tim thay phan tu {key1} trong mang")


key2 = 5
kqua2 = binary_search(arr, 0, len(arr) - 1, key2)

if kqua2 != -1:
    print(f"vi tri tim thay {key2} la: {str(kqua2)}")
else:
    print(f"khong tim thay phan tu {key2} trong mang")
