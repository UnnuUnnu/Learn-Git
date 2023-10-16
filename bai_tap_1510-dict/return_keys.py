key = input("nhap key: ").split(" ")
value = input("nhap value: ").split(" ")
if len(key) == len(value):  # điều kiện để tạo ra 1 dict mới
    dict1 = {}  # noi chứa các phần tử key: value
    for i in range(len(key)):
        dict1[key[i]] = value[i]  # key và value tương ứng sẽ thêm vào dict1
    a = []  # dung join method khi đó các key mới cách nhau -, dẫn đến nên phải có list để chứa
    sum = 0
    try:
        for j in dict1:  # vòng lap chạy hết các phân tủ trong dict 1
            a.append(str(j))  # thêm key vào list a
            # dict1[j] lấy value của thèn key, rồi cộng lại,  kiểu int bởi tính sum thì value phải là số
            sum = sum+int(dict1[j])
        print("-".join(a))  # in key ra màn hình cách nhau -
        print(sum)
    except:
        print("vui long nhap value so nguyen")
else:
    print("nhap chieu dai key=value")
