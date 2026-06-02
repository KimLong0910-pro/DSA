def split_array(a, k):
    left = max(a)
    right = sum(a)

    while left < right:
        mid = (left + right) // 2

        so_doan = 1
        tong = 0

        for so in a:
            if tong + so > mid:
                so_doan += 1
                tong = 0

            tong += so

        if so_doan <= k:
            right = mid
        else:
            left = mid + 1

    return left


a = [7, 2, 5, 10, 8]
k = 2
tong_lon_nhat = split_array(a, k)
print(f"Tổng lớn nhất nhỏ nhất: {tong_lon_nhat}")
