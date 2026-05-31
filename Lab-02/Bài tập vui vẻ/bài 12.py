def peak_element(a):
    left = 0
    right = len(a) - 1
    mid = 0

    while left < right:
        mid = (left + right) // 2

        if a[mid] < a[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


a = [1, 2, 3, 1]
vi_tri = peak_element(a)
print(f"Vị trí: {vi_tri}")
