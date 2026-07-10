stack = []


def tinh_hau_to(bieu_thuc=""):
    dau_in_math = bieu_thuc.split()

    for dau in dau_in_math:
        if dau.isdigit():
            stack.append(int(dau))
        else:
            a = stack.pop()
            b = stack.pop()

            if dau == "+":
                stack.append(a + b)

            elif dau == "-":
                stack.append(a - b)

            elif dau == "*":
                stack.append(a * b)

            elif dau == "/":
                stack.append(a / b)

    return stack.pop()


print(tinh_hau_to("3 4 + 2 *"))
