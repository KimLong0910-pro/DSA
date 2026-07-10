def S_hcn_max(chieu_cao):
    stack = []
    dtich_max = 0

    chieu_cao.append(0)

    for i in range(len(chieu_cao)):
        while stack and chieu_cao[stack[-1]] > chieu_cao[i]:
            h = chieu_cao[stack.pop()]

            if stack:
                w = i - stack[-1] - 1
            else:
                w = i

            dtich_max = max(dtich_max, h * w)
        stack.append(i)
    chieu_cao.pop()

    return dtich_max


chieu_cao = [2, 1, 5, 6, 2, 3]
dtich = S_hcn_max(chieu_cao)

print(f"Diện tích lớn nhất: {dtich}")