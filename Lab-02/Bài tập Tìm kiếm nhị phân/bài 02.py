def ton_tai(a, x):
    left = 0
    right = len(a) - 1
    mid = 0


    while left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            return True

        if x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return False


a = [2, 4, 6, 8]
x = 5
vi_tri = ton_tai(a, x)
print(f"Vị trí của {x}: {vi_tri}")
