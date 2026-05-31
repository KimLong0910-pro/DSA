def tim_kiem(a, x):
    left = 0
    right = len(a) - 1
    mid = 0

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            return mid

        if a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    else:
        return -1


a = [1, 3, 5, 7, 9]
x = 7
vi_tri = tim_kiem(a, x)
print(f"Vị trí {x}: {vi_tri}")
