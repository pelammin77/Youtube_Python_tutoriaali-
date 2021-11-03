class Auto:
    def __init__(self, merkki,malli, vm):

        self.merkki = merkki
        self.malli = malli
        self.vuosimalli = vm


    def kaasuta(self, n=1):
        print("nopeus kasvaa "+ str(n))


    def jarruta(self, n=1):
        print("Nopeus vähenee "+ str(n))




class PakettiAuto(Auto):

    def __init__(self, merkki,malli, vm, korkeus, tilavuus):
        super().__init__(merkki, malli, vm)
        self.tilavuus = tilavuus
        self.korkeus = korkeus


class PoliisiAuto(Auto):

    def kayta_sireenia(self):
        print("Pii paa")

class Maija(PoliisiAuto, PakettiAuto):
    def __init__(self,oma_argumentti, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.oma = oma_argumentti






maija = Maija("Poolisi maija","WW", "Transporter", vm=2020, korkeus= 2.5, tilavuus=10)
print(maija.oma)
maija.kayta_sireenia()


auto = Auto("Opel", "Astra", 2000)


