# Cách 1:
stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(f"top1: {stack[-1]}")
print(f"pop1: {stack.pop()}")
print(f"isEmpty1: {len(stack) == 0}")


# Cách 2:
stack2 = []


def push(data):
    stack2.append(data)


def pop():
    if len(stack2) == 0:
        return None
    else:
        return stack2.pop()


def top():
    if len(stack2) == 0:
        return None
    else:
        return stack2[-1]


def isEmpty():
    return len(stack2) == 0


push(1)
push(2)
push(3)
print(stack2)
print(f"pop2: {pop()}")
print(f"top2: {top()}")
print(f"isEmpty2: {isEmpty()}")
