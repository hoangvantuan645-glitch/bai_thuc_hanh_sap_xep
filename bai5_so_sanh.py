import random


def nhap_danh_sach(thong_bao_n="Nhập số lượng n: ", thong_bao_ds="Nhập các số nguyên (cách nhau bởi dấu cách): "):
    n = int(input(thong_bao_n))
    while True:
        ds = list(map(int, input(thong_bao_ds).split()))
        if len(ds) == n:
            return ds
        print(f"Cần nhập đúng {n} số, bạn nhập {len(ds)} số. Nhập lại nhé.")


def bubble_dem(a):
    a = a[:]
    so_sanh = hoan_doi = 0
    n = len(a)
    for i in range(n - 1):
        da_doi = False
        for j in range(n - 1 - i):
            so_sanh += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                hoan_doi += 1
                da_doi = True
        if not da_doi:
            break
    return a, so_sanh, hoan_doi


def insertion_dem(a):
    a = a[:]
    so_sanh = dich_chuyen = 0
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0:
            so_sanh += 1
            if a[j] > x:
                a[j + 1] = a[j]
                dich_chuyen += 1
                j -= 1
            else:
                break
        a[j + 1] = x
    return a, so_sanh, dich_chuyen


def selection_dem(a):
    a = a[:]
    so_sanh = hoan_doi = 0
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            so_sanh += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            hoan_doi += 1
    return a, so_sanh, hoan_doi


def thong_ke(ten_bo, ds):
    print(f"\n--- {ten_bo} ---")
    print(f"{'Thuật toán':<16}{'So sánh':>10}{'Hoán đổi/Dịch chuyển':>24}")
    for ten, ham in [("Bubble Sort", bubble_dem),
                     ("Insertion Sort", insertion_dem),
                     ("Selection Sort", selection_dem)]:
        kq, ss, hd = ham(ds)
        assert kq == sorted(ds)
        print(f"{ten:<16}{ss:>10}{hd:>24}")


def bai5():
    print("\n=== Bài 5. So sánh hiệu quả các thuật toán sắp xếp ===")
    ds = nhap_danh_sach()
    print("Danh sách vừa nhập:", ds)
    for ten, ham in [("Bubble Sort", bubble_dem),
                     ("Insertion Sort", insertion_dem),
                     ("Selection Sort", selection_dem)]:
        kq, ss, hd = ham(ds)
        print(f"{ten:<16}-> {kq} | so sánh: {ss}, hoán đổi/dịch chuyển: {hd}")

    n = len(ds)
    thong_ke("Đã sắp xếp tăng dần", list(range(n)))
    thong_ke("Sắp xếp giảm dần", list(range(n, 0, -1)))
    thong_ke("Dữ liệu ngẫu nhiên", random.sample(range(n * 10), n))
    print("\nNhận xét:")
    print("- Đã sắp xếp: Bubble (có cờ dừng sớm) và Insertion chỉ ~n so sánh; Selection vẫn ~n(n-1)/2.")
    print("- Giảm dần (xấu nhất): Bubble và Insertion đều ~n(n-1)/2 lần đổi/dịch; Selection chỉ ~n/2 lần hoán đổi.")
    print("- Ngẫu nhiên: Insertion thường ít thao tác hơn Bubble; Selection ít hoán đổi nhất.")


bai5()
