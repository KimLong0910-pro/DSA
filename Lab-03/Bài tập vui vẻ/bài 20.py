def dem_nghich_the(a):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2

        left, count_left = merge_sort(arr[:mid])
        right, count_right = merge_sort(arr[mid:])

        i = j = 0
        count = count_left + count_right
        kqua = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                kqua.append(left[i])
                i += 1
            else:
                kqua.append(right[j])
                count += len(left) - i
                j += 1

        kqua.extend(left[i:])
        kqua.extend(right[j:])

        return kqua, count

    _, count = merge_sort(a)

    return count


a = [2, 3, 1]
so_swap = dem_nghich_the(a)
print(f"Số swap của Bubble Sort: {so_swap}")
