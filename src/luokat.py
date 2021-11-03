class Tyontekija:
    """
    Tämä on worker luokka

    """

    def __init__(self, etunimi, sukunimi):
        '''
        This is  class's __init__
        :param etunimi:
        :param sukunimi:

        '''
        print("Luodaan objekti", self)
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.email = etunimi + '.'+ sukunimi + '@firma.fi'
    #
    def __del__(self):
        '''
        luokan del funktio
        '''
        #print("Olio",self,"tuhotaan")
        #print("Tallennetaan")

    def tulosta_tiedot(self):
        '''
        Metodi tulostaa luokan tiedot
        '''
        print()
        print("Tiedot")
        print('='*10)
        print("Nimi:",self.etunimi, self.sukunimi)
        print("Sähköposti:",self.email)

#
# t1 = Tyontekija("Pete", "Meikäläinen")
# t2 = Tyontekija("Matti", "Heijölöinen")
# print(t1)
# print(t2)
#
# t1.etunimi = "Matti"
# t1.sukunimi = "Meikäläinen"
# print(t1.etunimi)


def fun1():
    '''

    :return:
    '''
    print("Fun1")

if __name__ == '__main__':


#
      tekija1 = Tyontekija("Matti", "Meikäläinen")
      tekija2 = Tyontekija("Pekka", "Virtanen")

      # print(tekija1)
      # print(tekija2)
      # print(tekija1.etunimi, tekija1.sukunimi)
      # print(tekija1.email)
      # #tekija1.etunimi="Kimmo"
      # print(tekija1.etunimi, tekija1.sukunimi)
      # print(tekija1.email)
      #
      # tekija1.tulosta_tiedot()
      # Tyontekija.tulosta_tiedot(tekija2)
      print(tekija1.__doc__)
      print(tekija1.__init__.__doc__)
#