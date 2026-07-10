def early_exit(a):
    n = len(a)
    so_luot = 0

    for i in range(n - 1):
        da_doi_cho = False

        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                da_doi_cho = True
        
        if da_doi_cho:
            so_luot += 1
        else: 
            break
            

    return so_luot


a = [1, 2, 3, 5, 4]
kqua = early_exit(a)
print(kqua)
