class Koira:
    def __init__(self, nimi, omistaja):
        self.__nimi = nimi
        self.__omistaja = omistaja

    @property
    def nimi(self):
        return self.__nimi

    @nimi.setter
    def nimi(self, nimi):
        if len(nimi)>2:
            self.__nimi = nimi

    @nimi.deleter
    def nimi(self):
        del self.__nimi





    def get_omistaja(self):
        return self.__omistaja

    def set_omistaja(self, nimi):
        self.__omistaja = nimi

    def del_omistaja(self):
        del self.__omistaja


    omistaja = property(get_omistaja, set_omistaja, del_omistaja)


k1 = Koira("Tessu", "Pete")

print(k1.nimi)

k1.nimi = "Väpä"
print(k1.nimi)

print(k1.omistaja)

k1.omistaja = "Jukka"
print(k1.omistaja)






