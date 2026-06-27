def do_uu_tien(dau):
    if dau in "+-":
        return 1
    if dau in "*/":
        return 2
    else:
        return 0


def trung_so_sang_hau_to(bieu_thuc=""):
    stack = []
    output = []

    for ky_tu in bieu_thuc:
        if ky_tu.isalnum():
            output.append(ky_tu)
        else:
            while stack and do_uu_tien(stack[-1]) >= do_uu_tien(ky_tu):
                output.append(stack.pop())

            stack.append(ky_tu)

    while stack:
        output.append(stack.pop())

    return " ".join(output)


print(trung_so_sang_hau_to("a+b*c"))
