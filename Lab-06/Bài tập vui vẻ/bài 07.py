stack = []
stack_min = []


def push(nums):
    stack.append(nums)

    if len(stack_min) == 0 or nums <= stack_min[-1]:
        stack_min.append(nums)


def pop():
    if len(stack)==0:
        return None
    else: 
        data = stack.pop()

    if data == stack_min[-1]:
        stack_min.pop()

    return data

def getMin():
    if len(stack_min)==0:
        return None
    else: 
        return stack_min[-1]


push(5)
push(3)
push(7)
print(pop())
print(getMin())




