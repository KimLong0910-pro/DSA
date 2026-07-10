stack = []


def duyet_va_dem(ds):
    for i in ds:
        stack.append(i)

    stack_2 = []
    dem = 0

    while len(stack) > 0:
        x = stack.pop()
        print(x)

        stack_2.append(x)
        dem += 1

    while len(stack_2) > 0:
        stack.append(stack_2.pop())

    print(f"số phần tử: {dem}")
    return stack


ds = [1, 2, 3]
print(duyet_va_dem(ds))
