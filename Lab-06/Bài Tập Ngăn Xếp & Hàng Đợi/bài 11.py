class solution:
    def next_greater(self, arr):
        n = len(arr)
        kqua = [-1] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()

            if stack:
                kqua[i] = stack[-1]

            stack.append(arr[i])

        return kqua


s = solution()
print(s.next_greater([2, 1, 3]))
