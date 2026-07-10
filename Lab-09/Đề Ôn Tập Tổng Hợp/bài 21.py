def ktra(chuoi):
    stack = []
    cap = {")": "(", "]": "[", "}": "{"}

    for ky_tu in chuoi:
        if ky_tu in "([{":
            stack.append(ky_tu)
        else:
            if not stack or stack.pop() != cap[ky_tu]:
                return False

    return len(stack) == 0


chuoi = "([]{})"
kqua = ktra(chuoi)

print(f"Chuỗi '{chuoi}' cân bằng: {kqua}")
