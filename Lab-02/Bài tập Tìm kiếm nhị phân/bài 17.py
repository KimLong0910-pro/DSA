def ship_packages(w, D):
    left = max(w)
    right = sum(w)

    while left < right:
        mid = (left + right) // 2
        so_ngay = 1
        tong = 0

        for khoi_luong in w:
            if tong + khoi_luong > mid:
                so_ngay += 1
                tong = 0

            tong += khoi_luong

        if so_ngay <= D:
            right = mid
        else:
            left = mid + 1

    return left


w = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
D = 5
suc_chua = ship_packages(w, D)
print(f"Sức chứa nhỏ nhất: {suc_chua}")
