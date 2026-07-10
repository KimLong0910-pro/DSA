def gnome_sort(a):
    i = 0
    thao_tac = 0

    while i < len(a):
        if i == 0 or a[i] >= a[i - 1]:
            i += 1
        else:
            a[i], a[i - 1] = a[i - 1], a[i]
            thao_tac += 1
            i -= 1

    return a, thao_tac


a = [3, 2, 1]

kqua, thao_tac = gnome_sort(a)

print(f"Kết quả: {kqua}")
print(f"Số swap: {thao_tac}")