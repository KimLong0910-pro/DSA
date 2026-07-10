def tim_min_idx(a, i):
    min_idx = i

    for j in range(i + 1, len(a)):
        if a[j] < a[min_idx]:
            min_idx = j

    return min_idx


a = [9, 3, 7, 1, 5]
i = 1
kqua = tim_min_idx(a, i)

print(kqua)
