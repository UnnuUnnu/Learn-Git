key1 = input("nhap key1: ").split(" ")
value1 = input("nhap value1: ").split(" ")
key2 = input("nhap key2: ").split(" ")
value2 = input("nhap value2: ").split(" ")
if len(key1) == len(value1) and len(key2) == len(value2):
    dict1 = {}
    dict2 = {}
    for i in range(len(key1)):
        dict1[key1[i]] = value1[i]

    for i in range(len(key2)):
        dict2[key2[i]] = value2[i]

    if len(dict1) < len(dict2):
        dict2.update(dict1)  # dict2 cập nhật dict 1 vào
        print(dict2)
    else:
        dict1.update(dict2)  # dict1 cập nhật dict2 vào
        print(dict1)
else:
    print("moi ban nhap lai")
