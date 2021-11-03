# print("Hello")
# print("world")


numerot = [1 ,2,3]
#
# for i in range(1,101):
#     numerot.append(i)
#
# print(numerot)



# numerot_2 = [j for j in range(1, 101)]
# print(numerot_2)

# #
#
# sqr = []
#
# for i in range(1, 101):
#     sqr.append(i ** 2)
# #
# print(sqr)
# #
# sqr_2 = [i ** 2 for i in range(1,101)]
# print(sqr_2)
#
#
#
#
# #
# #
#
#
# nimet= ["Mika", "Petri", "Saku", "Juha", "Timo"]
# uusi_lista = []
#
# for nimi in nimet:
#   if "i" in nimi:
#     uusi_lista.append(nimi)
# print(uusi_lista)
#
# #
# uusi_lista = [nimi for nimi in nimet if "a" in nimi]
# #
# print(uusi_lista)
#
#
# dict_tyhja = {}
# #
# numeroiden_neliot_dict = {x : x ** 2  for x in range(1,101)}
# #
# print(numeroiden_neliot_dict)


tiedot_dict = {
    "etu_nimi" : "  Petri  ",
    "suku_nimi": "Lamminaho    ",
    "email": "   pete@mail.fi"
}

clean_tiedot_dict = {key : value.strip() for key, value in tiedot_dict.items()}
#
print(tiedot_dict)
print(clean_tiedot_dict)






