# sử dụng sort() tuy nhiên dạng str không có sắp xếp tăng dần, riêng số thì có, lưu ý là

a = ["khong", "gi", "la", "khong", "the"]
b = []
b = a.sort()
print(b)


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


# sort decending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)
