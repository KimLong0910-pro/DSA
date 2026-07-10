def insertion_shift(a):
    n = len(a)
    shift = 0

    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            shift += 1
            j -= 1

        a[j + 1] = key

    return shift


a = [1, 2, 4, 3, 5]

ban_dau = a.copy()
shift = insertion_shift(a)

print(f"Mảng ban đầu: {ban_dau}")
print(f"Mảng sau sort: {a}")
print(f"Số shift: {shift}")