import heapq


def dijkstra(do_thi):
    hang = len(do_thi)
    cot = len(do_thi[0])
    khoang_cach = [[float("inf")] * cot for _ in range(hang)]
    khoang_cach[0][0] = do_thi[0][0]
    huong = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    heap = [(do_thi[0][0], 0, 0)]

    while heap:
        chi_phi, x, y = heapq.heappop(heap)

        if chi_phi > khoang_cach[x][y]:
            continue

        for dx, dy in huong:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < hang and 0 <= ny < cot:
                new = chi_phi + do_thi[nx][ny]

                if new < khoang_cach[nx][ny]:
                    khoang_cach[nx][ny] = new
                    heapq.heappush(heap, (new, nx, ny))

    return khoang_cach[hang - 1][cot - 1]


do_thi = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
chi_phi = dijkstra(do_thi)

print(f"Tổng chi phí nhỏ nhất: {chi_phi}")
