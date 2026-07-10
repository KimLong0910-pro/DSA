class solution:
    def histogram(self, cao):
        stack = []
        dien_tich_max = 0
        cao.append(0)

        for i in range(len(cao)):
            while stack and cao[stack[-1]] > cao[i]:
                h = cao[stack.pop()]

                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i

                dien_tich = h * w
                dien_tich_max = max(dien_tich_max, dien_tich)

            stack.append(i)

        return dien_tich_max


s = solution()
print(s.histogram([2,1,5,6,2,3]))