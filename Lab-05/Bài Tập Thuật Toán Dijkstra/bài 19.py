import heapq


def xac_suat_max(do_thi, s, t):
    n = len(do_thi)
    xs_best = [0] * n
    xs_best[s] = 1

    heap = [(-1, s)]

    while heap:
        xs_u, u = heapq.heappop(heap)
        xs_u = -xs_u

        if u == t:
            return xs_u

        for v, xs in do_thi[u]:
            xs_new = xs_u * xs

            if xs_new > xs_best[v]:
                xs_best[v] = xs_new
                heapq.heappush(heap, (-xs_new, v))

    return 0


g1 = [[(1, 0.5), (2, 0.8)], [(3, 0.7)], [(3, 0.9)], []]
kqua = xac_suat_max(g1, 0, 3)

print(kqua)
