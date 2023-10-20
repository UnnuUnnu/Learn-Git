#https://howkteam.vn/course/bai-tap-python-tu-luyen/tra-ve-dict-ket-qua-da-sap-xep-theo-gia-tri-value-tang-dan-tham-so-la-1-dict-4238
key = [1, "hoa", "lan"]
value = [2, -1, 0]
dict1 = {}
allvalue_dict1 = []
dict1new = {}
for i in range(len(key)):
    dict1[key[i]] = value[i]
for j in dict1:
    allvalue_dict1.append(dict1[j])
    allvalue_dict1.sort()
for i in allvalue_dict1: