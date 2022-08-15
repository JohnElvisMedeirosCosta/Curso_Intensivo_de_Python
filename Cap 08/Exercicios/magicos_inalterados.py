def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "o grande " + magicians[i]

magicians = ['alberto', 'josé', 'john', 'carlos', 'marcelo']

great_magicians = magicians[:]

make_great(great_magicians)

show_magicians(great_magicians)
show_magicians(magicians)