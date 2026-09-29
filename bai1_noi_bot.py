def nhap_danh_sach(thong_bao_n="Nhập số lượng n: ", thong_bao_ds="Nhập các số nguyên (cách nhau bởi dấu cách): "):
    n = int(input(thong_bao_n))
    while True:
        ds = list(map(int, input(thong_bao_ds).split()))
        if len(ds) == n:
            return ds
        print(f"Cần nhập đúng {n} số, bạn nhập {len(ds)} số. Nhập lại nhé.")


def bubble_sort(a):
    a = a[:]
    n = len(a)
    for i in range(n - 1):
        da_doi = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                da_doi = True
        if not da_doi:
            break
    return a


def bai1():
    print("\n=== Bài 1. Sắp xếp nổi bọt ===")
    diem = nhap_danh_sach("Nhập số lượng điểm n: ", "Nhập các điểm (0-10): ")
    print("Danh sách trước khi sắp xếp:", diem)
    print("Danh sách sau khi sắp xếp:  ", bubble_sort(diem))


bai1()
