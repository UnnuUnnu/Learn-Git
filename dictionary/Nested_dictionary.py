# create 1 ditionary that contains several dictionary
# chucvu = {"cap 1": {"nhan vien": 3, "thuc tap": 2}, "cap 2": {"leader": 2}, "cap 3": {"giam doc": 1, "CEO": 2}

#           }
# print(chucvu)

# add several dictionaries into a new dictionary
# a = {"hoa": "gio", "co": 3}
# b = {"muon": "kiep", "nhan": "sinh", "co": 3, "bo": "tat ca"}
# c = {"tay": "lam", "ham": "nhai"}
# tonghop = {"a": a, "b": b, "c": c}
# print(tonghop)


# a = {"ban": "hong"}
# b = {"ban": "lan"}
# c = {"a": a,
#      "b": b

#      }
# print(c)

d = {"a": {"ban": "hong", "ten": "nga"},
     "b": {"tay": "lam", "ham": "nhai"}
     }
print(d)
c = d["b"]["ham"]
print(c)
