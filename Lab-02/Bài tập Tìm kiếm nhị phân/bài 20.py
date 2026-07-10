def book_allocation(p, m):
    left = max(p)
    right = sum(p)

    while left < right:
        mid = (left + right) // 2

        hs = 1
        tong_trang = 0

        for trang in p:
            if tong_trang + trang > mid:
                hs += 1
                tong_trang = 0

            tong_trang += trang

        if hs <= m:
            right = mid
        else:
            left = mid + 1

    return left


p = [12, 34, 67, 90]
m = 2
so_trang = book_allocation(p, m)
print(f"Số trang tối đa nhỏ nhất: {so_trang}")