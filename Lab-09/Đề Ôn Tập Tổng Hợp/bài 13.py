def dem_nghich_the(a):
    if len(a) <= 1:
        return a, 0

    mid = len(a) // 2
    left, nghich_the_left = dem_nghich_the(a[:mid])
    right, nghich_the_right = dem_nghich_the(a[mid:])
    kqua = []
    i = 0
    j = 0
    nghich_the = nghich_the_left + nghich_the_right

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            kqua.append(left[i])
            i += 1
        else:
            kqua.append(right[j])
            nghich_the += len(left) - i
            j += 1

    kqua.extend(left[i:])
    kqua.extend(right[j:])

    return kqua, nghich_the


a = [2, 4, 1, 3, 5]
mang_sap_xep, so_nghich_the = dem_nghich_the(a)

print(f"Mảng sau khi sắp xếp: {mang_sap_xep}")
print(f"Số nghịch thế: {so_nghich_the}")