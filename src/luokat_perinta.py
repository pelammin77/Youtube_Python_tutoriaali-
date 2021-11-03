class Lemmikki:

    def __init__(self, nimi, omistaja):

        self.nimi = nimi
        self.omistaja = omistaja


    def tulosta_tiedot(self):
        print(self.nimi)
        print(self.omistaja)


class Koira(Lemmikki):
    def __init__(self, nimi, omistaja, rotu):
        super().__init__(nimi, omistaja)
        #Lemmikki.__init__(self, nimi,omistaja)
        self.rotu = rotu

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(self.rotu)

    def hauku(self):
        print("Hau hau")




# lem = Lemmikki('Seppo', 'Musti')
#
# lem.tulosta_tiedot()


seppo = Koira("Seppo", "Musti", "Suomen pystykorva")

seppo.tulosta_tiedot()
seppo.hauku()