import heapq


def heuristic(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(grid):
    hang = len(grid)
    cot = len(grid[0])

    vo_cuc = float("inf")

    dist = [[vo_cuc] * cot for _ in range(hang)]
    dist[0][0] = grid[0][0]

    heap = []
    heapq.heappush(heap, (grid[0][0], grid[0][0], 0, 0))

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    visited_nodes = 0

    while heap:
        f_cost, g_cost, x, y = heapq.heappop(heap)
        visited_nodes += 1

        if x == hang - 1 and y == cot - 1:
            return g_cost, visited_nodes

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < hang and 0 <= ny < cot:
                new_cost = g_cost + grid[nx][ny]

                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost

                    h = heuristic(nx, ny, hang - 1, cot - 1)
                    f = new_cost + h

                    heapq.heappush(heap, (f, new_cost, nx, ny))

    return -1, visited_nodes


g1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
cost, visited = a_star(g1)

print(f"Shortest cost: {cost}")
print(f"Visited nodes: {visited}")
