def bubble_sort(a):
    n = len(a)
    lan_so_sanh = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                lan_so_sanh += 1

    return lan_so_sanh


a = [3,2,1]
kqua = bubble_sort(a)
print(kqua)
