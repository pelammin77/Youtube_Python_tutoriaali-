from collections import Counter

lista =["Petri", "Jukka", "Juha", "Saku", "Saku", "Ville", "Mikko", "Jukka", "Saku", "Petri", "Keijo", "Keijo" ]
lista2 =["Mikko", "Pekka", "Jukka"]

counter_1 = Counter(lista)
counter_2 = Counter(lista2)
#
print(counter_1)
#
# print(counter_1["Matti"])
# #
print(counter_1.most_common(2))
#
yhteen = counter_1 + counter_2
#
print(yhteen)
#
counter_2["Mikko"] = 10
print(counter_2)
#del counter_2["Mikko"]
#print(counter_2)
#
#
takaisin_lista = list(counter_2.elements())
#
print(takaisin_lista)
#
#
