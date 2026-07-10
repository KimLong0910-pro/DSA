import heapq


def toi_da_k_canh(do_thi, s, t, k):
    heap = [(0, s, 0)]

    while heap:
        cost, u, edges = heapq.heappop(heap)

        if u == t:
            return cost

        if edges == k:
            continue

        for v, weight in do_thi[u]:
            heapq.heappush(heap, (cost + weight, v, edges + 1))

    return -1


g1 = [[(1, 3), (2, 1)], [(3, 5)], [(3, 2)], []]
kqua = toi_da_k_canh(g1, 0, 3, 2)

print(kqua)
