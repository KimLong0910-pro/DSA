def mergeSorted(arr1, arr2):
    i = 0
    j = 0
    kqua = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            kqua.append(arr1[i])
            i += 1
        else:
            kqua.append(arr2[j])
            j += 1

    while i < len(arr1):
        kqua.append(arr1[i])
        i += 1

    while j < len(arr2):
        kqua.append(arr2[j])
        j += 1

    return kqua


a = [1, 3, 5]
b = [2, 4]

print(mergeSorted(a, b))
