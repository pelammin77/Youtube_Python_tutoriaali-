# #
# try:
#     with open("lista_with.txt", 'r') as f:
#         #uusi_lista = f.readlines()
#         uusi_lista = f.read().splitlines()
#         print()
#         print(uusi_lista)
#         print(type(uusi_lista))
#
# except FileNotFoundError:
#     print("Virheellinen tiedoston nimi")
#
# else:
#      print("Tiedoston lukeminen onnistui")
#

#

try:
     f = open("lista_with.txt", 'r')
     uusi_lista = f.read().splitlines()
     print()
     print(uusi_lista)
     print(type(uusi_lista))

except FileNotFoundError:
    print("Virheellinen tiedoston nimi")


else:
     print("Tiedoston lukeminen onnistui")

finally:
    try:
        f.close()
        print("Tiedosto suljetaan")
    except:
        pass




# x=0
# if x == 0:
#   raise Exception("Nollalla ei voi jakaa")

#
# x =  2.2
#
# if not type(x) is int:
#   raise TypeError("Annettu muuttujan on oltava luku")
#
# print(x)
