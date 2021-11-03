def str2list(str, erotin=' '):
    lst = list(str.split(erotin))
    lst = list(filter(None, lst))
    return lst

lause1 = "Ohjelmointi on mukavaa"
pitempi_teksti = "Aloitin ohjelmoinin 80-luvulla. Ensimmäinen kieleni oli Basic."

sanat_lista =  str2list(lause1)

print(type(sanat_lista))
print(sanat_lista)

lause_lista = str2list(pitempi_teksti,'.')
print(lause_lista)

uusi_mjono = ' '.join(sanat_lista)

print(uusi_mjono)

mj = ""

for w in sanat_lista:
    mj += w + " "

    print(mj)


nimi_jono = "     Petri    Lamminaho    "
nimi_jono = nimi_jono.lower()
print(nimi_jono)

print(len(nimi_jono))
nimi_jono = nimi_jono.strip()
print(nimi_jono)
print(len(nimi_jono))

rep_jono = "Petri, Saku, Keke, Juha, Jukka"

rep_jono = rep_jono.replace(',', ' Pilkku')
print(rep_jono)
