m, n = (input("nhap m va n lan luot: ").split(" "))
# m1 = {1, 2, 3, 4, 5}
# m2 = {"hoa", 1, "lan", "ba", 4}
# m3 = {"na", 1, 3, "bon,6"}
# setnew = set()
# for i in m1:
#     if i in m2 and i in m3:
#         setnew.add(i)
# print(setnew)
danhsach2chieu = []
if m.isnumeric() and n.isnumeric() and int(m) > 0 and int(n) > 0:
    print("nhap danh sach hai chieu kich thuoc mxn:")
    for i in range(int(m)):
        hang = input("nhap gia tri vao: ").split(" ")
        if len(hang) != n:
            print("danh sach 2 chieu khong dung kich thuoc")
        else:
            danhsach2chieu.append(hang)
else:
    print("Vui long nhap m va n >0")
