def early_exit(a):
    n = len(a)
    so_luot1 = 0

    for i in range(n - 1):
        da_doi_cho = False
        so_luot1 += 1
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                da_doi_cho = True
        if not da_doi_cho:
            break

    return so_luot1


a = [2, 1, 3, 4]
kqua = early_exit(a)
print(kqua)
