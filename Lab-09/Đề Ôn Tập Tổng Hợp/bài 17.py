import heapq


def dijkstra(do_thi, bdau):
    n = len(do_thi)
    khoang_cach = [float("inf")] * n
    khoang_cach[bdau] = 0
    heap = [(0, bdau)]

    while heap:
        chi_phi, node = heapq.heappop(heap)

        if chi_phi != khoang_cach[node]:
            continue

        for ke, trong_so in do_thi[node]:
            new = chi_phi + trong_so

            if new < khoang_cach[ke]:
                khoang_cach[ke] = new
                heapq.heappush(heap, (new, ke))

    return khoang_cach


do_thi = [[(1, 10), (2, 3)], [(3, 2)], [(1, 1), (3, 8)], [(4, 7)], []]
khoang_cach = dijkstra(do_thi, 0)

print(f"Khoảng cách ngắn nhất: {khoang_cach}")
