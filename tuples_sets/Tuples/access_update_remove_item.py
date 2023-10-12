# a = (123, "muon", "neo", 23)
# b = a[-4:-2]
# print(b)
# if 123 in a:
#     print("Yes, 123 is in the a")
# else:
#     print("No")


# update tuples

# a = ("nhan", "qua", 67, 96, "lam")
# b = list(a)
# b.append("hoa")
# b = tuple(a)
# print(b)

danh_sach1 = ("nhan", "qua", 123, 4)
danh_sach2 = ("tay", "lam", "ham", "nhai")
danh_sachmoi = danh_sach1+danh_sach2
print(danh_sachmoi)

# remove tuple-> covert tuple to list->tuple
a = ("muon", "neo", "duong", "que", )
b = list(a)
# b.remove("neo")
# a = tuple(b)
# print(a)

b.pop(0)
a = tuple(b)
print(a)
