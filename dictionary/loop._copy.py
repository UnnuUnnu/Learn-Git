a = {"hoa": "lan", "no": "ro", "vao": 3, "thang": "truoc"}

# return the keys value of the dictionary -> use keys()
# cach 1
# for i in a.keys():
#     print(i)

# cach 2
# for i in a:
#     print(i)


# return the values of the dictionary --> use values()
# # cach 1
# for i in a.values():
#     print(i)

# # cach 2
# for i in a:
#     print(a[i])

# return keys and values of the dictionary -> use items()

# for i, j in a.items():
#     print(i, j)


# copy dictionary

b = {"thanh": "cong", "bang": "voi", "no": "luc", "may": "man", "ca": 2}
# c = b.copy()
c = dict(b)
print(c)
