class YlaLuokka:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class AlaLuokka(YlaLuokka):
    def __init__(self, x, y, z):
        self.z = z

        super().__init__(x,y)


yla = YlaLuokka(10, 15)

ala =AlaLuokka(5, 7,10)

print(yla.x)
print(yla.y)

print(ala.z)
print(ala.x)
print(ala.y)


