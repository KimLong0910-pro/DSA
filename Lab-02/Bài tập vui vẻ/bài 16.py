def koko(pile, h):
    left = 1
    right = max(pile)

    while left < right:
        mid = (left + right) // 2
        total_time = 0

        for dong in pile:
            total_time += (dong + mid - 1) // mid

        if total_time <= h:
            right = mid
        else:
            left = mid + 1

    return left


pile = [3, 6, 7, 11]
h = 8
x = koko(pile, h)
print(f"tốc độ nhỏ nhất ăn trong {h} giờ: {x}")
