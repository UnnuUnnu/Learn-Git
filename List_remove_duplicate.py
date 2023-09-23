a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 89, 35, 55, 8]
list_remove_duplicate = []
for i in a:
    if i not in list_remove_duplicate:
        list_remove_duplicate.append(i)
print("list_remove_duplicate: ", list_remove_duplicate)
