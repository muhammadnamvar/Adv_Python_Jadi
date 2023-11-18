
print("$$$$$$$$$$$$$$$$$$$ Lambda arges: exp $$$$$$$$$$$$$$$$$$$$")


print("$$$$$$$$$$$$$$$$$$$$$$ Sort() $$$$$$$$$$$$$$$$$$$$$$$")
my_list = [23, 12, 3, 454, 1, 64, 74, 234]

my_list.sort()
print(my_list)

my_list4 = [(1, 5), (3, 2), (23, 11), (9, 3)]
my_list4.sort()
print(my_list4)

my_list4.sort(key=lambda x: x[1])
print(my_list4)


print("$$$$$$$$$$$$$$$$$$$ map() and filter() $$$$$$$$$$$$$$$$$$$$")
my_list2 = list(map(lambda x: x*2, my_list))
print(my_list2)

my_list3 = list(filter(lambda x: True if x % 2 == 0 else False, my_list))
print(my_list3)
