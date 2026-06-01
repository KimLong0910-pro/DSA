def gas_station(x, k):
    left = 0
    right = x[-1] - x[0]
    mid = 0

    while right - left > 1e-6:
        mid = (left + right) / 2

        can_them = 0

        for i in range(1, len(x)):
            can_them += int((x[i] - x[i - 1]) / mid)

        if can_them > k:
            left = mid
        else:
            right = mid

    return right


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 9
khoang_cach = gas_station(x, k)
print(f"Khoảng cách lớn nhất nhỏ nhất: {khoang_cach:.6f}")
