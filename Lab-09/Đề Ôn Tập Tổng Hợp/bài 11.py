def selection_sort(a):
    n = len(a)
    so_sanh = 0

    for i in range(n - 1):
        vi_tri_nho_nhat = i

        for j in range(i + 1, n):
            so_sanh += 1

            if a[j] < a[vi_tri_nho_nhat]:
                vi_tri_nho_nhat = j

        a[i], a[vi_tri_nho_nhat] = a[vi_tri_nho_nhat], a[i]

    return so_sanh


a = [5, 3, 4, 1, 2]
so_sanh = selection_sort(a)

print(f"Mảng sau khi sắp xếp: {a}")
print(f"Số phép so sánh: {so_sanh}")