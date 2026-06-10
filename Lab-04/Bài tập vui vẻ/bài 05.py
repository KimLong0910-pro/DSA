def insertion_s(a):
    n = len(a)
    so_lan_hoan_doi = 0 

    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            so_lan_hoan_doi += 1
            j = j - 1
        a[j + 1] = key


    return so_lan_hoan_doi


a = [3,2,1]
kqua= insertion_s(a)
print(kqua)