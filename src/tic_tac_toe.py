lauta = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

lauta_keys = []
for key in lauta:
    lauta_keys.append(key)




def piirra_lauta(lauta):
    print(lauta['7'] + '|' + lauta['8'] + '|' + lauta['9'])
    print('-----')
    print(lauta['4'] + '|' + lauta['5'] + '|' + lauta['6'])
    print('-----')
    print(lauta['1'] + '|' + lauta['2'] + '|' + lauta['3'])




def pelaa():
    vuoro ='X'
    vuoro_num = 0
    for i in range(10):
        piirra_lauta(lauta)
        print('On ',vuoro, ' vuoro tee siirto')
        siirto = input()
        if lauta[siirto] == ' ':
            lauta[siirto] = vuoro
            vuoro_num +=1
        else:
            print("Laiton siirto yritä uudelleen")
            continue

        if vuoro_num >=5:

            if lauta['7']==lauta['8']==lauta['9'] !=' ':
                piirra_lauta(lauta)
                print('Peli loppui\n')
                print(vuoro,"voitti")
                break

            elif lauta['4'] == lauta['5'] == lauta['6'] != ' ':
                piirra_lauta(lauta)
                print('Peli loppui\n')
                print(vuoro, "voitti")
                break

            elif lauta['1']==lauta['2']==lauta['3'] !=' ':
                piirra_lauta(lauta)
                print('Peli loppui\n')
                print(vuoro,"voitti")
                break

            elif lauta['1'] == lauta['4'] == lauta['7'] != ' ':
                piirra_lauta(lauta)
                print('Peli loppui\n')
                print(vuoro, "voitti")
                break

            elif lauta['2'] == lauta['5'] == lauta['8'] != ' ':
                piirra_lauta(lauta)
                print('Peli loppui\n')
                print(vuoro, "voitti")
                break

            elif lauta['3'] == lauta['6'] == lauta['9'] != ' ':
                piirra_lauta(lauta)
                print('Peli loppui\n')
                print(vuoro, "voitti")
                break

            elif lauta['3'] == lauta['5'] == lauta['7'] != ' ':
                piirra_lauta(lauta)
                print('Peli loppui\n')
                print(vuoro, "voitti")
                break

            elif lauta['1'] == lauta['5'] == lauta['9'] != ' ':
                piirra_lauta(lauta)
                print('Peli loppui\n')
                print(vuoro, "voitti")
                break

        if vuoro_num == 9:
            print("Peli loppui")
            print("Tasapeli")
            break




        if vuoro == 'X':
            vuoro ='O'

        else:
            vuoro='X'

    restart = input("Pelataanko uudelleen(k/e")
    if restart == 'k' or restart == 'K':
        for key in lauta:
            lauta[key]=" "
        pelaa()


if __name__ == '__main__':
    pelaa()