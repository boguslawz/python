def hypervolume(*args):
    print(args)
    print(type(args))

# hypervolume(1,2,3)


def hypervolue_second(*lengths):
    #mnozy wszystko po kolei
    i = iter(lengths)
    v = next(i)
    for length in i:
        v *= length
    return v


i = iter((1,2,3,4))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

print("hypervolue_second:")
print(hypervolue_second(1,2,3))