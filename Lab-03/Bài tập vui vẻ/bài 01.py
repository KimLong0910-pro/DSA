def one_pass(a):
    n = len(a)
    for i in range(n):
        da_doi = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                da_doi = True
            if not da_doi:
                break
    return a


a = [5, 1, 4, 2, 8]
kqua = one_pass(a)
print(kqua)