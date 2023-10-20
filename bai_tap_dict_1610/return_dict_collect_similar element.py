# https://howkteam.vn/course/bai-tap-python-tu-luyen/tra-ve-dict-ket-qua-bang-cach-gom-nhom-cac-phan-tu-giong-nhau-cua-list-theo-mau-tham-so-la-1-danh-4240
a = input("nhap chuoi ").split(" ")
dict1 = {}
for i in a:
    if i not in dict1.keys():
        dict1[i] = [i]
    else:
        dict1[i].append(i)
print(dict1)
