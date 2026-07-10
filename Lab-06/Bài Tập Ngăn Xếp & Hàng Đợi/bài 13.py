class solution:
    def dfs(self, do_thi, bdau):
        stack = [bdau]
        visited = set()

        while stack:
            dinh = stack.pop()

            if dinh not in visited:
                print(dinh, end=" ")
                visited.add(dinh)

                for i in reversed(do_thi[dinh]):
                    stack.append(i)


do_thi = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [],
    5: []
}

s = solution()
s.dfs(do_thi, 1)