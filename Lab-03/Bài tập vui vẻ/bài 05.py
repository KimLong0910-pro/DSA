def bubble_sort(a):
    n = len(a)
    so_lan_so_sanh = 0
    
    for i in range(n-1):
        for j in range(n - 1 - i):
            so_lan_so_sanh += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return so_lan_so_sanh


a = [1, 2, 3]
kqua = bubble_sort(a)
print(kqua)
