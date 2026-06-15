def selection_stats(a):
    n = len(a)
    so_sanh = 0
    swap = 0

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            so_sanh += 1

            if a[j] < a[min_idx]:
                min_idx = j

        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swap += 1

    return so_sanh, swap


best = [1, 2, 3, 4, 5]
avg = [3, 5, 1, 4, 2]
worst = [5, 4, 3, 2, 1]

print(f"Best: {selection_stats(best.copy())}")
print(f"Average: {selection_stats(avg.copy())}")
print(f"Worst: {selection_stats(worst.copy())}")