l = [i * 2 for i in range(10)]
print("lista generowana z wyrazenia:")
print(l)

class Trace:
    def __init__(self):
        self.enabled = True
    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap

result = map(Trace()(ord), 'The quick brown fox.')
print(result)

#map nie generuje wartosci z siebie, tylko trzeba je wywolac
print(next(result))
print(next(result))
print(next(result))

print("*******   USING MAP:")
print(list(map(ord, "The downhill")))
print("*******   USING FOR:")

for o in map(ord, "the downhill"): print(o)

pierwszy = ['a' , 'b', 'c']
drugi = ['d' , 'e', 'f']

def combine(pierw, drug):
    return '{} {}'.format(pierw, drug)

#list po to zeby byly dostarczone wartosci, bez list jest tylko obiekt typu map
a = list(map(combine, pierwszy, drugi))
print("Uzycie map:")
print(a)