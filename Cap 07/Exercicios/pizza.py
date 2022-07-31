ingredientes = []
while True:
    message = input("Pressione 'quit' para sair.\nInsira os ingredientes: ")

    if message == 'quit':
        break
    print("Esse ingrediente será adicionado à pizza!")
    ingredientes.append(message)

print('Ingredientes da pizza: ')
for ingrediente in ingredientes:
    print("\t" + ingrediente)