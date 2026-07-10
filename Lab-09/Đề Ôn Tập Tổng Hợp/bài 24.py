def next_greater(a):
    stack = []
    kqua = [-1] * len(a)

    for i in range(len(a) - 1, -1, -1):
        while stack and stack[-1] <= a[i]:
            stack.pop()

        if stack:
            kqua[i] = stack[-1]

        stack.append(a[i])

    return kqua


a = [2, 1, 3]
kqua = next_greater(a)

print(f"Kết quả: {kqua}")
