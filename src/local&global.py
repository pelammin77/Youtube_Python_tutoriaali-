
from my_pack.hello import moro

moro('Pete')



x = 0
VAKIO = 10

tarkea_tieto = 10


def func1():

    x =10

    global tarkea_tieto
    global VAKIO

    VAKIO =20

    tarkea_tieto = 20
    #x = 10

    print(x)

    def sisa_func():
        print(x)
    sisa_func()
    print(x)






print(x)
func1()

print(x)