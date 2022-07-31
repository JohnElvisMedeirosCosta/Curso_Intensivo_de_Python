pessoa_1 = {
    'first_name' : 'John',
    'last_name' : 'Costa',
    'age' : 26,
    'city': 'São Paulo'
}

pessoa_2 = {
    'first_name' : 'maria',
    'last_name' : 'josé',
    'age' : 56,
    'city': 'rio de janeiro'
}

pessoa_3 = {
    'first_name' : 'antonio',
    'last_name' : 'lima',
    'age' : 36,
    'city': 'pernambuco'
}

pessoas = [pessoa_1, pessoa_2, pessoa_3]

for pessoa in pessoas:
    print("\nDados sobre " + pessoa['first_name'].title() + ":")

    print("\tFirst Name: " + pessoa['first_name'].title())
    print("\tLast Name: " + pessoa['last_name'].title())
    print("\tAge: " + str(pessoa['age']))
    print("\tCity: " + pessoa['city'].title())
