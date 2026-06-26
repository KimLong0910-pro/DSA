stack = []


def push(nums):
    stack.append(nums)
    return stack


def pop():
    if len(stack) == 0:
        return None
    else:
        return stack.pop()


print(f"thêm: {push(5)}")
print(f"thêm: {push(7)}")

print(f"lấy ra: {pop()}")
print(f"mảng còn lại khi được lấy ra: {stack}")
