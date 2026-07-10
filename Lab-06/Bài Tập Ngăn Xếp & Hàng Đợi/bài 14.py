class solution:
    def stock_span(self, gia):
        stack = []
        kqua = []

        for i in range(len(gia)):
            while stack and gia[stack[-1]] <= gia[i]:
                stack.pop()

            if not stack:
                span = i + 1
            else:
                span = i - stack[-1]

            kqua.append(span)
            stack.append(i)

        return kqua


s = solution()
print(s.stock_span([100,80,60,70,60,75,85]))