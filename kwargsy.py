def tag(name, **attributes):
    for key, value in attributes.items():
        print("key: {k}, values: {v}.".format(k=key, v=str(value)))

slownik = {'owoc': "jablko ", 'warzywo': 'pietrucha'}

tag("warzywniak", owoc = "jablko ", warzywo = 'pietrucha')

def print_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)

t = (1, 2, 3, 4)
# *t to wtedy on sobie sam da arg1 i 2 a z reszty zrobi tuple (extended Call Syntax)
print_args(*t)

def color(red, green, blue, **kwargs):
    print('r =', red)
    print('g =', green)
    print('b =', blue)
    print(kwargs)

k = {'red':21, 'green':68, 'blue':120, 'alpha':52}

print("extended call function kwargs example!")
color(**k)

slownik = dict(red=21, blue=44)
print(slownik)

#kwargsy uzywane do przekierownia
def f(*args, **kwargs):
    print("args =", args)
    print("kwargs =", kwargs)

def trace(functition_def, *args, **kwargs):
    f(*args, **kwargs)

trace(f, 'ff', 'gg', base = 16, name = 'IBM')