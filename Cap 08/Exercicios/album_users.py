
def make_album(artista, titulo_album, num_faixas=''):
    album = {
        'artista': artista,
        'titulo_album': titulo_album
    }
    if num_faixas:
        album['faixa'] = num_faixas

    return album

while True:
    print("\nInsira os dados do album")
    print("Caso queira encerrar o programa a qualquer momento, "
          "basta digitar 'q'")

    artista = input('Insira o nome do artista: ')
    if artista.lower() == 'q':
        break

    album = input('Insira o nome do album: ')
    if album.lower() == 'q':
        break

    print(make_album(artista, album))