def can_bac_hai_nguyen(n):
    left = 0
    right = n
    mid = 0
    kqua = 0

    while left <= right:
        mid = (left + right) // 2

        if mid**2 <= n:
            kqua = mid
            left = mid + 1
        else:
            right = mid - 1

    return kqua


n = int(input("Nhập số n: "))
kqua_can = can_bac_hai_nguyen(n)
print(f"Kết quả căn của {n}: {kqua_can}")
