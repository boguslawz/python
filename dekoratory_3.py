def check(func):
    def inside(a, b):
        if b == 0:
            print("Can't divide by 0.")
            return
        # print(func(a, b))
        func(a, b)
    return inside

@check
def div(a, b):
    return a/b

# div = check(div)

print(div(4,0))