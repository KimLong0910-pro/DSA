def insertion_s_stability(a):
    n = len(a)

    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0:
            if len(key) < len(a[j]):
                a[j + 1] = a[j]
                j -= 1
            else:
                break

        a[j + 1] = key

    return a


a = ["abc", "a", "ab"]

kqua = insertion_s_stability(a.copy())

print(f"Mảng ban đầu: {a}")
print(f"Kết quả: {kqua}")
