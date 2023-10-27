setx = set(input("Nhap set x: ").split(" "))
sety = set(input("Nhap set \y: ").split(" "))
setxnew = set()
setynew = set()
for i in setx:
    if i not in sety:
        setxnew.add(i)
for i in sety:
    if i not in setx:
        setynew.add(i)
print("set x not contain character set y", " ".join(setxnew))
print("set y not contain character set x", " ".join(setynew))
