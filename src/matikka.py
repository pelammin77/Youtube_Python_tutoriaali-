from math import pi

def ympyran_ala(r):
    if type(r) not in[int, float]:
        raise TypeError("Säteen on oltava reaaliluku")
    if r<0:
        raise ValueError("Sääteen on oltava positiivinen luku")

    return pi*(r**2)


# sateet =[2, 0,-2, "2"]
# for r in sateet:
#
#     ala = ympyran_ala(r)
#
#     print(ala)
#
