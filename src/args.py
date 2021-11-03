# *args[]
# **kwargs

#
# def tulosta_argumentit(otsikko, infoa, *args):
#     print(otsikko)
#     print(infoa)
#     print(len(args))
#
#     for post in args:
#         print(post)
# #
# # #
# # #
# # #
# # #
# blogin_otsikko = "Peten it blogi"
# tulosta_argumentit(blogin_otsikko,"Pete kirjoittaa ohjelmoinnista ", "Tämä on ensimmäinen postaus", "Toinen postaus",
#                    "Kolmas postaus", "viimeinen postaus")
#

#
# def print_kwargs(otsikko, lisa,**kwargs):
#     print(otsikko)
#     print(lisa)
#     for key, value in kwargs.items():
#         print(key,':', value)
# #
# #
# # #
# print_kwargs("Henkkarit", "lisatiedot",Nimi="Pete",email="pete@gamail.com", ika=40)
# #
#
import matplotlib.pyplot as plt

x1 =[0, 2, 4]
y1 = [0, 4, 8]
grap_args = [x1, y1]




def piirra_plotti(x, y ):
    plt.plot(x, y)
    plt.show()
#
#
#
#
#
piirra_plotti(x1,y1)
# #
# #
piirra_plotti(*grap_args)
# #
# #
# #
# #
