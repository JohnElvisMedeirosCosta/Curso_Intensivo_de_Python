lupi = {
    'nome' : 'lupi',
    'tipo' : 'cachorro',
    'dono' : 'john'
}

leao = {
    'nome' : 'leao',
    'tipo' : 'cachorro',
    'dono' : 'joyce'
}

billy = {
    'nome' : 'billy',
    'tipo' : 'gato',
    'dono' : 'camila'
}

pets = [lupi, leao, billy]

for pet in pets:
    print("\nDados sobre o " + pet['nome'].title() + ":")
    print("\tNome: " + pet['nome'].title())
    print("\tTipo: " + pet['tipo'].title())
    print("\tDono: " + pet['dono'].title())