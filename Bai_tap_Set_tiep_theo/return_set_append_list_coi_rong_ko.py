set1 = set(input(" nhap set: ").split(" "))
list2 = input("nhap danh sach: ").split(" ")
set2new = set(list2)
# set1.update(set2new)
# print(set1)
for i in set2new:
    if i not in set1:
        set1.add(i)
print(set1)
# nếu nhập list rỗng kết quả lại có rỗng làm sau?
