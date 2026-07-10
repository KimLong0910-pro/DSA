def rpn(bieu_thuc):
    stack = []

    for token in bieu_thuc.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(a // b)

    return stack.pop()


bieu_thuc = "3 4 + 2 *"
kqua = rpn(bieu_thuc)

print(f"Kết quả: {kqua}")
