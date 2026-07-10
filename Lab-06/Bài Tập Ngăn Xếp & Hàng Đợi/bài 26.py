class solution:
    def window_max(self, nums, k):
        deque = []
        kqua = []

        for i in range(len(nums)):
            while deque and deque[0] <= i - k:
                deque.pop(0)

            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()

            deque.append(i)

            if i >= k - 1:
                kqua.append(nums[deque[0]])

        return kqua


s = solution()
print(s.window_max([1,3,-1,-3,5,3], 3))