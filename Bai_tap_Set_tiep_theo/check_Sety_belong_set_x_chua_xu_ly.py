setx = set(input("Nhap set x: ").split(" "))
sety = set(input("Nhap set y: ").split(" "))
isError = False
if len(sety) > len(setx):
    print(False)
else:
    for i in sety:
        if i in setx:
            isError = True
    if isError == True:
        print(True)
# tại sao chiue dai x=y lại khonogra kết quả
