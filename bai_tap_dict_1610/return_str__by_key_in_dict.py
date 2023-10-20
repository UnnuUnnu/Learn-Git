a = input("nhap chuoi: ").split(" ")
key = input("nhap key: ").split(" ")
value = input("nhap value: ").split(" ")
dict1 = {}
if len(key) == len(value):
    for i in range(len(key)):
        dict1[key[i]] = value[i]
    # for i in a: (nếu làm như này kết quả lại không đúng tại sao)
    #     for j in dict1.keys():
    #         if i in j:
    #             i = dict1[j]
    for i in range(len(a)):
        for j in dict1.keys():
            if a[i] in j:
                a[i] = dict1[j]
    print(dict1)
    print("chuoi sau khi thay thế các từ có key trong dict : ", " " .join((a)))
else:
    print("moi nhap chieu dài key=value")
