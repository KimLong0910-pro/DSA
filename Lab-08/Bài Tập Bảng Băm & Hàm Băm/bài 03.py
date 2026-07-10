def dem_tan_suat(arr):
    kqua = {}

    for x in arr:
        if x in kqua:
            kqua[x] += 1
        else:
            kqua[x] = 1

    return kqua


arr = ["a", "b", "a", "c", "a"]
print(dem_tan_suat(arr))
