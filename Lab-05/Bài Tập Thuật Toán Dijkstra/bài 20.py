import heapq


def k_shortest(do_thi, s, t, k):
    heap = [(0, s)]
    dem = {}
    dap_an = []

    while heap:
        dist_u, u = heapq.heappop(heap)

        dem[u] = dem.get(u, 0) + 1

        if u == t:
            dap_an.append(dist_u)
            if len(dap_an) == k:
                return dap_an

        if dem[u] > k:
            continue

        for v, weight in do_thi[u]:
            heapq.heappush(heap, (dist_u + weight, v))

    return dap_an


g1 = [[(1, 1), (2, 2)], [(3, 4)], [(3, 3)], []]
kqua = k_shortest(g1, 0, 3, 3)

print(kqua)
