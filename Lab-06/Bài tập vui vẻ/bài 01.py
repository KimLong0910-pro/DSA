# # Cách 1:
# stack = []

# stack.append(1)
# stack.append(2)
# stack.append(3)

# print(f"top1: {stack[-1]}")
# print(f"pop1: {stack.pop()}")
# print(f"isEmpty1: {len(stack) == 0}")


# # Cách 2:
# stack2 = []


# def push(data):
#     stack2.append(data)


# def pop():
#     if len(stack2) == 0:
#         return None
#     else:
#         return stack2.pop()


# def top():
#     if len(stack2) == 0:
#         return None
#     else:
#         return stack2[-1]


# def isEmpty():
#     return len(stack2) == 0


# push(1)
# push(2)
# push(3)
# print(stack2)
# print(f"pop2: {pop()}")
# print(f"top2: {top()}")
# print(f"isEmpty2: {isEmpty()}")


# Cách 3
class stack111:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def overflow(self):
        return self.top == self.size - 1

    def push(self, nums):
        if self.overflow():
            print("full")
            return None

        self.top += 1
        self.arr[self.top] = nums

    def pop(self):
        if self.isEmpty():
            print("empty")
            return None

        temp = self.arr[self.top]
        self.arr[self.top] = None
        self.top -= 1
        return temp
    
if __name__ == '__main__':
    stack = stack111(4)

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(f'mảng: {stack.arr}')
    print(f'vị trí hiên tại: {stack.top}')

    pop1 = stack.pop()
    print(f'lấy ra: {pop1}')

    print(f'mảng: {stack.arr}')
    print(f'vị trí hiên tại: {stack.top}')


