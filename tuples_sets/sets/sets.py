a = {"hoa", 3, "lan", True}
print(a)

# sets cannot have 2 item with the same value
b = {"lan", "co", "nha", "lan"}
# print(b)
# print(len(b))
# print(type(a))

for i in a:
    print(i)
if "hoa" in a:
    print("yes, 'hoa' is in the set")
else:
    print("No")
