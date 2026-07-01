def indexOf(arr, goal):
    for i in range(len(arr)):
        if arr[i] == goal:
            return i
    return -1


arr = [5, 3, 7]
print(indexOf(arr, 7))
