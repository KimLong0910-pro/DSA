def gan_x_nhat(a, x):
    gia_tri_gan_nhat = a[0]
    vi_tri = 0
    do_lech_nho_nhat = abs(a[0] - x)

    for i in range(1, len(a)):
        do_lech = abs(a[i] - x)

        if do_lech < do_lech_nho_nhat:
            do_lech_nho_nhat = do_lech
            gia_tri_gan_nhat = a[i]
            vi_tri = i

    return gia_tri_gan_nhat, vi_tri



a = [10, 22, 28, 29, 40]
x = 26

gia_tri_gan_nhat, vi_tri = gan_x_nhat(a, x)

print(f"Giá trị gần x nhất: {gia_tri_gan_nhat} - Vị trí: {vi_tri}")
