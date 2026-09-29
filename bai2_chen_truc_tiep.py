def nhap_danh_sach(thong_bao_n="Nhập số lượng n: ", thong_bao_ds="Nhập các số nguyên (cách nhau bởi dấu cách): "):
    n = int(input(thong_bao_n))
    while True:
        ds = list(map(int, input(thong_bao_ds).split()))
        if len(ds) == n:
            return ds
        print(f"Cần nhập đúng {n} số, bạn nhập {len(ds)} số. Nhập lại nhé.")


def insertion_sort_in_trang_thai(a):
    a = a[:]
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x
        print(f"Chèn {x:>4} -> {a}  (phần đã sắp xếp: {a[:i + 1]})")
    return a


def bai2():
    print("\n=== Bài 2. Sắp xếp chèn trực tiếp ===")
    ma = nhap_danh_sach("Nhập số mã đơn hàng n: ", "Nhập các mã đơn hàng: ")
    print("Ban đầu:", ma)
    kq = insertion_sort_in_trang_thai(ma)
    print("Kết quả sau khi sắp xếp:", kq)


bai2()
