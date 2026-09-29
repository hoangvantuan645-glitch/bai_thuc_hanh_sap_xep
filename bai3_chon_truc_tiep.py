def nhap_danh_sach(thong_bao_n="Nhập số lượng n: ", thong_bao_ds="Nhập các số nguyên (cách nhau bởi dấu cách): "):
    n = int(input(thong_bao_n))
    while True:
        ds = list(map(int, input(thong_bao_ds).split()))
        if len(ds) == n:
            return ds
        print(f"Cần nhập đúng {n} số, bạn nhập {len(ds)} số. Nhập lại nhé.")


def selection_sort_in_trang_thai(a):
    a = a[:]
    n = len(a)
    so_sanh = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            so_sanh += 1
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        print(f"Lượt {i + 1}: {a}")
    return a, so_sanh


def bai3():
    print("\n=== Bài 3. Sắp xếp chọn trực tiếp ===")
    sbd = nhap_danh_sach("Nhập số lượng n: ", "Nhập các số báo danh: ")
    print("Ban đầu:", sbd)
    kq, so_sanh = selection_sort_in_trang_thai(sbd)
    print("Kết quả:", kq)
    print("Tổng số lần so sánh:", so_sanh)


bai3()
