def merge_count(a):
    n = len(a)
    if n <= 1:
        return a, 0

    mid = n // 2

    left, dem_left = merge_count(a[:mid])
    right, dem_right = merge_count(a[mid:])

    kqua = []
    i = 0
    j = 0
    dem = dem_left + dem_right

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            kqua.append(left[i])
            i += 1
        else:
            kqua.append(right[j])
            dem += len(left) - i
            j += 1

    kqua.extend(left[i:])
    kqua.extend(right[j:])

    return kqua, dem


a = [2, 4, 1, 3]

_, shift = merge_count(a)

print(f"Số shift: {shift}")