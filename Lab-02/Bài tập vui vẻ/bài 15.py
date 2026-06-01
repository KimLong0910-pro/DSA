def k_gan_nhat(a, k, x):
    left = 0
    right = len(a) - k
    mid = 0

    while left < right:
        mid = (left + right) // 2

        if x - a[mid] > a[mid + k] - x:
            left = mid + 1
        else:
            right = mid

    return a[left : left + k]


a = [1, 2, 3, 4, 5]
x = 3
k = 4
kqua = k_gan_nhat(a, k, x)
print(f"Kết quả: {kqua}")
