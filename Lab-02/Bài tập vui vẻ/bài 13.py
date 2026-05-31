def single_element(a):
    left = 0
    right = len(a) - 1
    mid = 0

    while left < right:
        mid = (left + right) // 2

        if mid % 2 == 1:
            mid -= 1

        if a[mid] == a[mid + 1]:
            left = mid + 2
        else:
            right = mid

    return a[left]


a = [1, 1, 2, 3, 3, 4, 4]
phan_tu = single_element(a)
print(f"Phần tử đơn lẻ: {phan_tu}")
