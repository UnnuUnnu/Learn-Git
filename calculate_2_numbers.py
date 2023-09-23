# https://howkteam.vn/course/bai-tap-python-tu-luyen/tinh-tong-hai-so-nguyen-bat-ky-co-xu-ly-ngoai-le-dau-vao-4102
while True:
    a = input("nhap a: ")
    b = input("nhap b: ")
    try:
        so1 = int(a)
        so2 = int(b)
        print("tong 2 so: ", so1+so2)
        break
    except:
        print("dau vao khong hop le")
