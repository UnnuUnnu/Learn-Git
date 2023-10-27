set1 = set((input("Input: ")).split(" "))
set1new = set()
for i in set1:
    if i.isnumeric():
        set1new.add(i)
set1.symmetric_difference_update(set1new)

print(set1)
