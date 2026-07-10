def bubble_sort(a):
    n = len(a)
    so_lan_hoan_doi = 0
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                so_lan_hoan_doi += 1

    return so_lan_hoan_doi


a = [3,2,1]
kqua = bubble_sort(a)
print(kqua)
