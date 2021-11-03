
def func(f):
    def wrapper(*args, **kwargs):
        print("Start")
        ret = f(*args, **kwargs)

        print("end")
        return ret
    return wrapper

@func
def apu_func1(x):
    print("olen apu1")
    print(x)

@func
def apu_func2(x, y):
    print("olen apu2")
    return x + y

apu_func1(5)
print(apu_func2(2, 4))
