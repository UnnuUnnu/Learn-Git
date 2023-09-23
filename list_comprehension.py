# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = input("Nhap danh sach thu nhat: ").split(",")
b = input("Nhap danh sach thu hai: ").split(",")
list_comprehension = []
for i in a:
    if i in b and i not in list_comprehension:
        list_comprehension.append(float(i))
print("list_comprehension: ", list_comprehension)
