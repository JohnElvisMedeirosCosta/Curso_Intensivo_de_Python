favorite_places = {
    'john' : ['são paulo'],
    'maria' : ['rio de janeiro', 'sao paulo'],
    'josé' : ['rio de janeiro']
}

for nome, place in favorite_places.items():
    if len(place) > 1:
       print("\nOs lugares favoritos do(a) " + nome.title() + ' é:')
       for place in place:
           print("\t" + place.title())
    else:
        print("\nO lugar favoritos do(a) " + nome.title() + ' é ' + place[0].title())