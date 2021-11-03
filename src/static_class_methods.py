import datetime

class TyonTekija:

    __tekija_lkm = 0



    def __init__(self, etu_nimi, suku_nimi, palkka):
        self.etu_nimi = etu_nimi
        self.suku_nimi = suku_nimi
        self.palkka = palkka
        TyonTekija.__lisaa_lkm()





    def get_tiedot(self):
        return "{} {} {}".format(self.etu_nimi,self.suku_nimi, str(self.palkka))

    @classmethod
    def __lisaa_lkm(cls):
        cls.__tekija_lkm += 1

    @classmethod
    def get_lkm(cls):
        return  cls.__tekija_lkm

    @staticmethod
    def onko_tyo_paiva(paiva):
        if paiva.weekday()== 5 or paiva.weekday() == 6:
            return False
        else:
            return True




print(TyonTekija.get_lkm())

t1 = TyonTekija("Matti", "Meikäläiinen", 3000)

t2 = TyonTekija("Teppo", "Teikalainen", 3000 )
print(t1.get_tiedot())

print(TyonTekija.get_lkm())

p = datetime.date(2021, 1, 10)

print(TyonTekija.onko_tyo_paiva(p))










