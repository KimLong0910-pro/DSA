def lien_tiep_dai_nhat(arr):
    tap = set(arr)
    max_len = 0

    for x in tap:
        if x - 1 not in tap:
            current = x
            do_dai = 1

            while current + 1 in tap:
                current += 1
                do_dai += 1

            max_len = max(max_len, do_dai)

    return max_len

arr = [100, 4, 200, 1, 3, 2]
print(lien_tiep_dai_nhat(arr))