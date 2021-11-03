# # nclass Testi:
# #     pass
# #
# # print(Testi)
# # print(Testi())
# # t = Testi()
# #
# # print(t)
# # print(type(5))
# # print(type(type))
#
# class Moro:
#     def sano_moro(self):
#         print("moro")
#
#
# def sano_terve(self):
#     print("terve")
#
# Testi = type("Testi",(Moro,), {"x":2, "y":3, "sano_terve": sano_terve})
#
# t =Testi()
#
# print(t)
# t.sano_moro()
# print(t.x)
# t.sano_terve()

class TestMeta(type):
    def __new__(cls, cls_name, bases, attrs):
        print("Luokka luotiin nimeltään:"+cls_name)
        print(attrs)

        return super().__new__(cls, cls_name, bases,attrs)


class TarkistaPienet(type):
    def __new__(cls, cls_name, bases, attrs):
        print(attrs)
        for name in attrs:
            if name.lower()!=name:
                raise TypeError("Virheellinen muuttujan nimi")

        return super().__new__(cls, cls_name, bases, attrs)







class Test(metaclass=TarkistaPienet):

     x = 5
     Y = 2
#
#
# t = Test()
# print(t)



p