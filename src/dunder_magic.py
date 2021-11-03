lista = [2, 3, 6]

class Ihminen:
    def __init__(self, nimi):
        self.nimi = nimi

    # def __repr__(self):
    #     return "Hei nimeni on "+ self.nimi
    #
    def __str__(self):
        return "Hei nimeni on "+ self.nimi

    def __call__(self, x, y):
        return x*y


    def __mul__(self, n):
        self.nimi = self.nimi * n







print(type(lista))

i1 = Ihminen("Pete")

print(type(i1))

#print(lista)
print(i1)
print(i1(2, 7))

i1*10

print(i1)
