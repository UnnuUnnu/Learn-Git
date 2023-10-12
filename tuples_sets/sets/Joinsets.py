# union() and update() will exclude any duplictae items (loai bo phan tu giong nhau giua 2 set)
# a = {"hoa", "co", "lan"}
# b = {"nang", "dep", "co"}
# tai sao khong dung duoc a.union(a)
# a.union(b)
# print(a)

# c = a.union(b)
# print(c)

# a.update(b)
# print(a)

# Keep only the duplicate item use intersection_update(), or intersection() method
# a = {"hoa", "co", "lan"}
# b = {"nang", "dep", "co"}
# #tai sao khong dung dươc
# a.intersection(b)
# print(a)

# c = a.intersection(b)
# print(c)

# a.intersection_update(b)
# print(a)

# keep all, but not the duplicate use symmetric_difference_update or symmetric_diffrence
a = {1, "hoa"}
b = {2, "hoa", "nang"}

# a.symmetric_difference_update(b)
# print(a)

# tai sao khong su dung duoc nhu duoi ma phai co 1 bien moi
# a.symmetric_difference(b)
# print(a)

c = a.symmetric_difference(b)
print(c)
