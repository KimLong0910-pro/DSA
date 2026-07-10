hang_doi_1 = []
hang_doi_2 = []


def push(nums):
    hang_doi_1.append(nums)


def pop():
    if len(hang_doi_1) == 0:
        return None

    while len(hang_doi_1) > 1:
        hang_doi_2.append(hang_doi_1.pop(0))

    data = hang_doi_1.pop(0)

    while len(hang_doi_2) > 0:
        hang_doi_1.append(hang_doi_2.pop(0))

    return data


push(1)
push(2)
push(3)

print(pop())
