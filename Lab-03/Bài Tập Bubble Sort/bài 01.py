def one_pass(a):
    n = len(a)

    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

    return a


a = [5, 1, 4, 2, 8]
kqua = one_pass(a)
print(kqua)
