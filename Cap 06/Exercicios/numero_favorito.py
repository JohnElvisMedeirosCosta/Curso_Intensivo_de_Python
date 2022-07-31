favorito = {
    'maria' : [10, 20],
    'joao' : [13, 22],
    'josé' : [44, 20],
    'anderson' : [26, 13],
    'josefa' : [11, 45]
}

for name, number in favorito.items():
    if len(number) > 1:
        print("Os números favoritos do(a) " + name.title() + " é:")
        for number in number:
            print("\t" + str(number))
