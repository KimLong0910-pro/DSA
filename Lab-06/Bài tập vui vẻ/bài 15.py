class solution:
    def sort_stack(self, stack):
        stack_phu = []

        while stack:
            temp = stack.pop()

            while stack_phu and stack_phu[-1] < temp:
                stack.append(stack_phu.pop())

            stack_phu.append(temp)

        return stack_phu


s = solution()
print(s.sort_stack([3,1,2]))