class Solution:
    def bfs(self, do_thi, bdau):
        queue = [bdau]
        visited = set([bdau])

        while queue:
            node = queue.pop(0)
            print(node, end=" ")

            for neighbor in do_thi[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


do_thi = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [],
    5: []
}

s = Solution()
s.bfs(do_thi, 1)