import heapq


# Partial Selection
def partial_selection(a, k):
    n = len(a)

    for i in range(min(k, n)):
        min_idx = i

        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j

        a[i], a[min_idx] = a[min_idx], a[i]

    return a[:k]


a = [7, 2, 5, 1, 9, 3]
k = 3

print(partial_selection(a.copy(), k))


# Heap
def heap_k_smallest(a, k):
    heapq.heapify(a)

    kqua = []

    for _ in range(k):
        kqua.append(heapq.heappop(a))

    return kqua


a = [7, 2, 5, 1, 9, 3]
k = 3

print(heap_k_smallest(a.copy(), k))
