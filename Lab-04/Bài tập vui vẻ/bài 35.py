def selection_sort(a):
    n = len(a)
    swap = 0

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j

        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swap += 1

    return swap


a = [1, 2, 3]
kqua = selection_sort(a)

print(kqua)
