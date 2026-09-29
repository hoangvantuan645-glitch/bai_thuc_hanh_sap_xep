def nhap_danh_sach(thong_bao_n="Nhập số lượng n: ", thong_bao_ds="Nhập các số nguyên (cách nhau bởi dấu cách): "):
    n = int(input(thong_bao_n))
    while True:
        ds = list(map(int, input(thong_bao_ds).split()))
        if len(ds) == n:
            return ds
        print(f"Cần nhập đúng {n} số, bạn nhập {len(ds)} số. Nhập lại nhé.")


def merge(trai, phai):
    kq = []
    i = j = 0
    while i < len(trai) and j < len(phai):
        if trai[i] <= phai[j]:
            kq.append(trai[i])
            i += 1
        else:
            kq.append(phai[j])
            j += 1
    kq.extend(trai[i:])
    kq.extend(phai[j:])
    return kq


def merge_sort(a):
    if len(a) <= 1:
        return a
    giua = len(a) // 2
    trai = merge_sort(a[:giua])
    phai = merge_sort(a[giua:])
    kq = merge(trai, phai)
    print(f"Hòa nhập {trai} + {phai} -> {kq}")
    return kq


def bai4():
    print("\n=== Bài 4. Sắp xếp hòa nhập ===")
    ds = nhap_danh_sach()
    print("Ban đầu:", ds)
    kq = merge_sort(ds)
    print("Danh sách sau khi sắp xếp tăng dần:", kq)


bai4()
