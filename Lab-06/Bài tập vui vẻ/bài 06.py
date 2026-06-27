def ktra_ngoac(chuoi):
    stack = []

    for ky_tu in chuoi:
        if ky_tu in "([{":
            stack.append(ky_tu)

        elif ky_tu in "}])":
            if len(stack) == 0:
                return False
            else:
                top = stack.pop()

            if ky_tu == ")" and top != "(":
                return False
            if ky_tu == "]" and top != "[":
                return False
            if ky_tu == "}" and top != "{":
                return False

    return len(stack) == 0


print(ktra_ngoac("([]{})"))
print(ktra_ngoac("([)]"))
print(ktra_ngoac("([{}])"))
