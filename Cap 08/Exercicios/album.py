def make_album(artista, titulo_album, num_faixas=''):
    if num_faixas:
        album = {
            'artista': artista,
            'titulo_album': titulo_album,
            'num_faixas': num_faixas
        }
    else:
        album = {
            'artista': artista,
            'titulo_album': titulo_album
        }
    return album

disco_1 = make_album('Mc Livinho', 'Fiquei louco')
disco_2 = make_album('Anitta', 'Poderosa')
disco_3 = make_album('Tiesto', 'Hello World', 25)

print(disco_1)
print(disco_2)
print(disco_3)