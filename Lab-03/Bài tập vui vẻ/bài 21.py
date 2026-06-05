def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j][0] > a[j + 1][0]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a


a = [(2, "a"), (1, "b"), (2, "c")]
kqua = bubble_sort(a)
print(kqua)
