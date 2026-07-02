def printElements(arr):
    for x in arr:
        print(x)


def countEven(arr):
    dem = 0
    for x in arr:
        if x % 2 == 0:
            dem += 1
    return dem


arr = [1, 2, 3, 4]
print(countEven(arr))
