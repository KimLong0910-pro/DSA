import heapq


def bottleneck(do_thi, s, t):
    n = len(do_thi)
    vo_cuc = float("inf")

    khoang_cach = [vo_cuc] * n
    khoang_cach[s] = 0

    heap = [(0, s)]

    while heap:
        dist_u, u = heapq.heappop(heap)

        if u == t:
            return dist_u

        for v, weight in do_thi[u]:
            new_dist = max(dist_u, weight)

            if new_dist < khoang_cach[v]:
                khoang_cach[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    return -1


g1 = [[(1, 4), (2, 2)], [(3, 5)], [(3, 3)], []]
kqua = bottleneck(g1, 0, 3)

print(kqua)
