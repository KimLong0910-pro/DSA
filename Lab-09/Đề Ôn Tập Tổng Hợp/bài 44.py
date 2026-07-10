def two_sum(arr, target):
    bang_bam = {}

    for i, x in enumerate(arr):
        bo_sung = target - x

        if bo_sung in bang_bam:
            return (bang_bam[bo_sung], i)

        bang_bam[x] = i

    return None

arr = [2, 7, 11]
target = 9

print(two_sum(arr, target))