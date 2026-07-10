def bubble_sort_abs(a):
    n = len(a)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if abs(a[j]) > abs(a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]

    return a


a = [-3, 1, -2, 2]
kqua = bubble_sort_abs(a)
print(kqua)
