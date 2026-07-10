import heapq


def dijkstra(do_thi, bdau):
    n = len(do_thi)
    khoang_cach = [float("inf")] * n
    parent = [-1] * n
    khoang_cach[bdau] = 0
    heap = [(0, bdau)]

    while heap:
        chi_phi, node = heapq.heappop(heap)

        if chi_phi > khoang_cach[node]:
            continue

        for ke, chi_phi in do_thi[node]:
            new = chi_phi + chi_phi

            if new < khoang_cach[ke]:
                khoang_cach[ke] = new
                parent[ke] = node
                heapq.heappush(heap, (new, ke))

    return khoang_cach, parent


do_thi = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5)], [(4, 3)], []]
bdau = 0
target = 4
khoang_cach, parent = dijkstra(do_thi, bdau)
duong_di = []

while target != -1:
    duong_di.append(target)
    target = parent[target]

duong_di.reverse()

print(f"Đường đi ngắn nhất: {duong_di}")
print(f"Tổng chi phí: {khoang_cach[4]}")
