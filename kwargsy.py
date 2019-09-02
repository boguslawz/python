def tag(name, **attributes):
    for key, value in attributes.items():
        print("key: {k}, values: {v}.".format(k=key, v=str(value)))

slownik = {'owoc': "jablko ", 'warzywo': 'pietrucha'}

tag("warzywniak", owoc = "jablko ", warzywo = 'pietrucha')