import copy

test_list_1 = [1, 2, 3]   # By default Python make surface copy of any object

lst1 = test_list_1
lst1[1] = 1000           # and if we change one of these 2 objects, both of them will change

print(test_list_1)
print(lst1)
print()

test_list_2 = [1, 2, 3]
lst2 = copy.copy(test_list_2)   # Using copy module we can retrieve a deepcopy of this object
lst2[1] = 1000

print(test_list_2)
print(lst2)
