stack = []


def dao_nguoc_chuoi(word):
    for character in word:
        stack.append(character)

    kqua = ""

    while len(stack) > 0:
        kqua += stack.pop()

    return kqua


word = "abc"
print(dao_nguoc_chuoi(word))
