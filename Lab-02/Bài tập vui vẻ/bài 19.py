def aggressive_cows(x, c):
    x.sort()

    left = 1
    right = x[-1] - x[0]
    mid = 0

    while left < right:
        mid = (left + right + 1) // 2

        da_dat = 1
        vi_tri_cuoi = x[0]

        for i in range(1, len(x)):
            if x[i] - vi_tri_cuoi >= mid:
                da_dat += 1
                vi_tri_cuoi = x[i]

        if da_dat >= c:
            left = mid
        else:
            right = mid - 1

    return left


x = [1, 2, 4, 8, 9]
c = 3
khoang_cach = aggressive_cows(x, c)
print(f"Khoảng cách lớn nhất: {khoang_cach}")
