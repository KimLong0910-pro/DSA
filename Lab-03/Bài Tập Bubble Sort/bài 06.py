def one_pass_cuoi(a):
    n = len(a)

    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
                
    return a[n - 1]


a = [4, 2, 7, 1, 3]
kqua = one_pass_cuoi(a)
print(kqua)
