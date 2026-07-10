from collections import deque


def max_window(a, k):
    deque_index = deque()
    kqua = []

    for i in range(len(a)):
        while deque_index and deque_index[0] <= i - k:
            deque_index.popleft()

        while deque_index and a[deque_index[-1]] <= a[i]:
            deque_index.pop()
        deque_index.append(i)

        if i >= k - 1:
            kqua.append(a[deque_index[0]])

    return kqua


a = [1, 3, -1, -3, 5, 3]
k = 3
kqua = max_window(a, k)

print(f"Giá trị lớn nhất mỗi cửa sổ: {kqua}")
