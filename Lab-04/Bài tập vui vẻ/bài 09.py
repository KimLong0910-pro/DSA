def sap_xep_chen(a):
    so_sanh = 0
    dich_chuyen = 0
    n = len(a)

    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0:
            so_sanh += 1
            if key < a[j]:
                a[j + 1] = a[j]
                dich_chuyen += 1
                j -= 1
            else:
                break

        a[j + 1] = key

    return so_sanh, dich_chuyen


def tim_vi_tri_chen_nhi_phan(a, left, right, key):
    so_sanh = 0

    while left <= right:
        mid = (left + right) // 2
        so_sanh += 1

        if key < a[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return left, so_sanh


def sap_xep_chen_nhi_phan(a):
    so_sanh = 0
    dich_chuyen = 0
    n = len(a)

    for i in range(1, n):
        key = a[i]
        vi_tri, dem = tim_vi_tri_chen_nhi_phan(a, 0, i - 1, key)
        so_sanh += dem

        j = i - 1
        while j >= vi_tri:
            a[j + 1] = a[j]
            dich_chuyen += 1
            j -= 1

        a[vi_tri] = key

    return so_sanh, dich_chuyen


a = [5, 2, 4, 6, 1, 3]

mang_thuong = a.copy()
mang_nhi_phan = a.copy()
so_sanh_thuong, dich_chuyen_thuong = sap_xep_chen(mang_thuong)
so_sanh_nhi_phan, dich_chuyen_nhi_phan = sap_xep_chen_nhi_phan(mang_nhi_phan)

print(f"Mảng ban đầu: {a}")
print(f"Insertion sort: {mang_thuong}")
print(f"So sánh: {so_sanh_thuong}")
print(f"Shift: {dich_chuyen_thuong}")

print(f"Binary insertion sort: {mang_nhi_phan}")
print(f"So sánh: {so_sanh_nhi_phan}")
print(f"Shift: {dich_chuyen_nhi_phan}")
