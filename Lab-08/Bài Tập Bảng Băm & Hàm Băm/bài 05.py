def group_by_chu_cai_dau(ds_tu):
    kqua = {}

    for tu in ds_tu:
        key = tu[0]

        if key not in kqua:
            kqua[key] = []

        kqua[key].append(tu)

    return kqua


ds_tu = ["apple", "ant", "banana", "ball", "cat"]

print(group_by_chu_cai_dau(ds_tu))
