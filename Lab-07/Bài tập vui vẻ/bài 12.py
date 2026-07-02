# Cách 1: O(n²)
def removeDuplicates_n2(arr):
    kqua = []

    for x in arr:
        found = False
        for y in kqua:
            if x == y:
                found = True
                break
        if not found:
            kqua.append(x)

    return kqua


# Cách 2: O(n)
def removeDuplicates(arr):
    seen = set()
    kqua1 = []

    for x in arr:
        if x not in seen:
            seen.add(x)
            kqua1.append(x)

    return kqua1


arr = [3, 1, 3, 2, 1]

print(removeDuplicates_n2(arr))
print(removeDuplicates(arr))
