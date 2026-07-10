def median_hai_mang(a, b):
    hop = sorted(a + b)
    n = len(hop)

    if n % 2 == 1:
        return float(hop[n // 2])
    else:
        return (hop[n // 2 - 1] + hop[n // 2]) / 2


a = [1, 3]
b = [2]
trung_vi = median_hai_mang(a, b)
print(f"Trung vị: {trung_vi}")
