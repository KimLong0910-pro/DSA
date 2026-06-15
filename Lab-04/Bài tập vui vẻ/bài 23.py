def thong_ke(a):
    n = len(a)
    so_sanh = 0
    shift = 0

    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0:
            so_sanh += 1

            if key < a[j]:
                a[j + 1] = a[j]
                shift += 1
                j -= 1
            else:
                break

        a[j + 1] = key

    return so_sanh, shift


best = [1, 2, 3, 4]
avg = [3, 1, 4, 2]
worst = [4, 3, 2, 1]

print(f"Best: {thong_ke(best.copy())}")
print(f"Average: {thong_ke(avg.copy())}")
print(f"Worst: {thong_ke(worst.copy())}")