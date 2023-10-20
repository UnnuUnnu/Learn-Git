a = input("nhap chuoi: ")
dict1 = {}
for i in a:
    if i not in dict1.keys():
        dict1[i] = 1
    else:
        dict1[i] += 1
print(dict1)
