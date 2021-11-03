VAKIO = 10
class Lemmikki:
    def __init__(self, nimi, omistaja):
        self.__nimi = nimi
        self._omistaja = omistaja

    def tulosta_tiedot(self):
        print(self.__nimi)
        print(self._omistaja)

    def __str__(self):
        pass
    





l1 = Lemmikki("Tessu", "Pete")



#l1._Lemmikki__nimi = "Jalo" # TÄTÄ EI SAA KÄYTTÄÄ!!!!
l1._omistaja ="Mika"

l1.tulosta_tiedot()