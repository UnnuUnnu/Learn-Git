key = input("nhap chuoi key: ").split(" ")
value = input("nhap chuoi value: ").split(" ")
if len(key) == len(value):
    dictnew = {}
    for i in range(len(key)):
        dictnew[key[i]] = value[i]
    print(dictnew)
else:
    print("moi nhap lai")
