def removeIfEven(arr):
    write = 0

    for read in range(len(arr)):
        if arr[read] % 2 != 0:
            arr[write] = arr[read]
            write += 1

    return arr[:write]


arr = [1, 2, 3, 4]
print(removeIfEven(arr))
