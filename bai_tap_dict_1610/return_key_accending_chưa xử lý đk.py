# https://howkteam.vn/course/bai-tap-python-tu-luyen/tra-ve-dict-ket-qua-da-sap-xep-theo-gia-tri-key-tang-dan-tham-so-la-1-dict-4237
key = input("nhap key la so nguyen: ").split(" ")
value = input("nhap value: ").split(" ")
if len(key) == len(value):
    dict1 = {}
    allkey_dict1 = []
    dict1new = {}
    for i in range(len(key)):
        dict1[key[i]] = value[i]
    for i in dict1:
        allkey_dict1.append(int(i))
        allkey_dict1.sort()
    for i in allkey_dict1:
        for j in dict1.keys():
            # if allkey_dict1[i] in dict1:
            dict1new[i] = dict1[j]
    print("danh sach sau khi xep", dict1new)
    print(dict1)
else:
    print("nhap chieu dai key==value")

# key = input("nhap key la so nguyen: ").split(" ")
# value = input("nhap value: ").split(" ")
# for i in key:
#     if i.isalpha():
#         print("vui long nhap key la so nguyen")
#     elif i.isnumeric() and len(key) == len(value):
#         dict1 = {}
#         allkey_dict1 = []
#         dict1new = {}
#         for i in range(len(key)):
#             dict1[key[i]] = value[i]
#         for i in dict1:
#             allkey_dict1.append(i)
#             allkey_dict1.sort()
#         for i in allkey_dict1:
#             dict1new[i] = dict1[i]
#         print(dict1)
#         print("danh sach sau khi xep", dict1new)
#     else:
#         print("nhap chieu dai key==value")
