
KERROIN = 5
#
# def tervehdys():
#      print("Hello Python")
#
#
# tervehdys()
#
#
# def tyhja_funktio():
#     pass



#
def tervehdys_usr(usr="Pete"):
     """
     Kuvaus:
     Tämä tulostaa terve

     :param usr:
     :return:
     """

     print("Terve",usr)
#
# tervehdys_usr()

#
# user = input("Anna nimi>")
# tervehdys_usr(usr=user)

#
#
def laske_yhteen(luku1, luku2):
     """
     Kuvaus:

     Tämä funktio laskee kaksi lukua yhteen ja
     palautaa tuloksen

     :param luku1: integer
     :param luku2:integer

     :return: luku1 + luku2: tulos: integer

     """

     return luku1 + luku2



def palauta_useampi_arvo(luku1, luku2):
     summa = luku1 + luku2
     tulo = luku1 * luku2
#
     return summa, tulo

#_, tulo = palauta_useampi_arvo(3,2)
#print(tulo)

#
#
def vakio_kerroin(kerrottava):
     return kerrottava * KERROIN


if __name__ == '__main__':

     #tervehdys()
    # print(vakio_kerroin(2))
     help(tervehdys_usr)


