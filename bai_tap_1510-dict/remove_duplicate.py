# khai báo đầu vào biến str thành list ngăn cách bỏi khoảng trống
key = input("nhap key: ").split(" ")
value = input("nhap value: ").split(" ")
if len(key) == len(value):  # điều kiện để tạo ra một dict
    dict1 = {}  # noi chứa các phần tử key:value
    # vòng lặp for để chạy hết các phần tử key,  bởi len(key) trả về số nên dùng range (len())
    for i in range(len(key)):
        # với mỗi key và value tương ứng sẽ thêm vào dict1
        dict1[key[i]] = value[i]

    dict2 = {}  # tạo ra một dict2 mới không chứa các value trùng nhau
    for j in dict1:  # dùng vòng lặp để chạy hết các phần tử key trong dict2
        # kiểm tra vaule của dict1 ko nằm trong tất cả value dict2 chưa
        if dict1[j] not in dict2.values():
            # value của dict1 sẽ thêm vào dict2, [j] đây là value
            dict2[j] = dict1[j]
    print(dict2)
else:  # nếu chiều dài của len và key khác nhau dict sẽ không tạo ra
    print("moi nhap lai: ")
