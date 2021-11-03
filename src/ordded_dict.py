from collections import OrderedDict

osakkeet =[('Nokia', 3.19), ('Apple', 132.75), ('Kone',66.48)]
osakkeet_2 = [('Apple', 132.75), ('Kone',66.48), ('Nokia', 3.19) ]
dict_1 = {}
dict_2 ={}

for name, value in osakkeet:
    dict_1[name] = value

for name, value in osakkeet_2:
    dict_2[name]= value
#
#
#
print(dict_1)
print( dict_2)
#
ord_dict_1 = OrderedDict(osakkeet)
ord_dict_2 = OrderedDict(osakkeet_2)
#
print(dict_1 == dict_2)
#
print(ord_dict_1 == ord_dict_2)
#



#
# print(dict_1.keys())
# print(dict_1.values())