def muuta_luku(luku):
    print("Luku on", luku)
    luku +=1
    print("Muokkauksen jälkeen", luku)

luku = 3
print("Ennen muokkausta luku on", luku)
muuta_luku(luku)
print("muokkauksen jälkeen luku =", luku)


#
# def muuta_nimi(nimi):
#     print('nimi on', nimi)
#     nimi = "pete"
#     print("Muokattu nimi=", nimi )
#     return  nimi
#
# glob_nimi = 'Petri'
#
# glob_nimi = muuta_nimi(glob_nimi)
# print("muutoksen jälkeen nimi = "+glob_nimi)

# def muokkaa_listaa(the_list):
#     print('lista', the_list)
#     the_list.append('Juha')
#     print('Muokattu', the_list)
#
# global_list = ['Pete', 'Saku', 'Keke']
#
# print('ensin, global_list =', global_list)
# muokkaa_listaa(global_list)
# print('lisäyksen jlkeen globaali lista, =', global_list)