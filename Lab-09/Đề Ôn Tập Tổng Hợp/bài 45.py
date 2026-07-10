def dem_doan_con(arr, k):
    dem = {0: 1}
    tong = 0
    kqua = 0

    for x in arr:
        tong += x

        if tong - k in dem:
            kqua += dem[tong - k]
        dem[tong] = dem.get(tong, 0) + 1

    return kqua


print(dem_doan_con([1, 1, 1], 2))
