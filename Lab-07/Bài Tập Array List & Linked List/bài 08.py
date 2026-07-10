def removeIfEven(arr):
    ghi = 0

    for doc in range(len(arr)):
        if arr[doc] % 2 != 0:
            arr[ghi] = arr[doc]
            ghi += 1

    return arr[:ghi]


arr = [1, 2, 3, 4]
print(removeIfEven(arr))
