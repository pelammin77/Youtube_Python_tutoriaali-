import argparse




def laske_pinta_ala(kanta, korkeus):

    return kanta * korkeus



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Tämä ohjelma laskee neliön pinta-alan")
    parser.add_argument("-w", "--kanta", type=int, help="Kanta", required=True)
    parser.add_argument("-H","--korkeus", type=int, help="Korkeus", required=True )
    args = parser.parse_args()

    res = laske_pinta_ala(args.kanta, args.korkeus)

    print(res)








    # kanta = 2
    # korkeus = 3
    #
    # res = laske_pinta_ala(kanta,korkeus)
    #
    # print("Neliön pinta-ala on on", res)


