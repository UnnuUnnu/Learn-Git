c = 4


def sum(a, b):
    # globbal c lay bien c o ben ngoai ham (c=4)
    # neu chi khai bao trong ham c=5 thi se hiu la bien local (chi su dung trong ham sum)
    global c
    c = 5
    return a+b+c


a = int(input("Nhap a: "))
b = int(input("nhap b: "))
print("tong 2 so la: ", sum(a, b))
print(c)
