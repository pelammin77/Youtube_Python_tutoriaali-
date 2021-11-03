
def functio(x):
    return 2*x+1

print(functio(5))

func = lambda x: 2*x+1
print(func(5))
#
def laske_yhteen(x, y):
    return x + y

print(laske_yhteen(5, 2))


func2 = lambda x,y : x+y

print(func2(5,2))
#
def kutsuu_laske_yhteen(x, y):
    return laske_yhteen(x,y)*10

#
#
#
#
def kutsuu_lambdaa(x,y):
    func2 = lambda x, y: x + y
    return func2(x, y)*10


print(kutsuu_laske_yhteen(5,2))
print(kutsuu_lambdaa(5,2))

