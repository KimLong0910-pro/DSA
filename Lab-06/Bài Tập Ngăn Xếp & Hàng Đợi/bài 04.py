stack = [None] * 3
top = -1

def push(data):
    global top
    
    if top == len(stack) - 1:
        print("Overflow")
        return
    
    top += 1
    stack[top] = data

    return stack

def pop():
    global top
    
    if top == -1:
        print("Underflow")
        return None
    
    data = stack[top]
    top -= 1
    return data

print(push(1))
print(push(2))
print(push(3))

print(pop())
print(pop())
print(pop())