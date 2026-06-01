def kth_missing(a, k):
    left = 0
    right = len(a)
    mid = 0

    while left < right:
        mid = (left + right) // 2

        if a[mid] - (mid + 1) < k:
            left = mid + 1
        else:
            right = mid

    return left + k


a = [2, 3, 4, 7, 11]
k = 5
bi_thieu = kth_missing(a, k)
print(f"Số nguyên dương thứ {k} bị thiếu: {bi_thieu}")
