def insertion_s(arr, x):
    n = len(arr)
    arr.append(x)
    
    key = arr[-1]
    j = n - 1

    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key


arr = [1, 3, 5, 7]
x = 4
insertion_s(arr, x)
print(arr)
