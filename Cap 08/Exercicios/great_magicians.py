def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

# Alterando o valor da lista utilziando a sua posição, o método index()
# retorna a posição do valor, assim ele é alterado de x para "o grande x".
# Essa função altera a lista original, é possível preserva-la utilizando uma
# lista de apoio
# def make_great(magicians):
#     for magician in magicians:
#         magicians[magicians.index(magician)] = "o grande " + magician

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "o grande " + magicians[i]

magicians = ['alberto', 'josé', 'john', 'carlos', 'marcelo']

make_great(magicians)

show_magicians(magicians)