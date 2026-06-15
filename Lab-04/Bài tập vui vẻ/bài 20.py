# Gap = n//2
def shell_sort(a):
    n = len(a)
    gap = n // 2
    shift = 0

    while gap > 0:
        for i in range(gap, n):
            key = a[i]
            j = i

            while j >= gap and key < a[j - gap]:
                a[j] = a[j - gap]
                shift += 1
                j -= gap

            a[j] = key

        gap //= 2

    return a, shift


a = [8, 5, 3, 7, 6, 2, 4, 1]

ban_dau = a.copy()
kqua, shift = shell_sort(a)

print(f"Mảng ban đầu: {ban_dau}")
print(f"Kết quả của n//2: {kqua}")
print(f"Số shift của n//2: {shift}")


# Dãy gap Knuth
def shell_sort_knuth(a):
    n = len(a)
    shift = 0

    gap = 1
    while gap < n // 3:
        gap = gap * 3 + 1

    while gap > 0:
        for i in range(gap, n):
            key = a[i]
            j = i

            while j >= gap and key < a[j - gap]:
                a[j] = a[j - gap]
                shift += 1
                j -= gap

            a[j] = key

        gap //= 3

    return a, shift


a = [8, 5, 3, 7, 6, 2, 4, 1]

ban_dau = a.copy()

kqua, shift = shell_sort_knuth(a)

print(f"Mảng ban đầu: {ban_dau}")
print(f"Kết quả của knuth: {kqua}")
print(f"Số shift của knuth: {shift}")
