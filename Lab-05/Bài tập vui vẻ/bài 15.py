import heapq


def dijkstra_grid(grid):
    hang = len(grid)
    cot = len(grid[0])

    vo_cuc = float("inf")

    dist = []  # Ma trận lưu khoảng cách nhỏ nhất từ ô bắt đầu đến từng ô

    for i in range(hang):  # Duyệt từng hàng
        current_row = []  # Tạo một hàng mới

        for j in range(cot):  # Duyệt từng cột trong hàng
            current_row.append(vo_cuc)  # Ban đầu mọi ô đều là vô cực
        dist.append(current_row)  # Thêm hàng vào ma trận dist

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    heap = [(grid[0][0], 0, 0)]
    dist[0][0] = grid[0][0]

    while heap:
        cost, x, y = heapq.heappop(heap)

        if x == hang - 1 and y == cot - 1:
            return cost

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < hang and 0 <= ny < cot:
                new_cost = cost + grid[nx][ny]

                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heapq.heappush(heap, (new_cost, nx, ny))

    return -1


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
kqua = dijkstra_grid(grid)

print(f"Minimum cost: {kqua}")
