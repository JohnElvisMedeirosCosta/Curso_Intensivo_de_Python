responses = {}

polling_active = True

while polling_active:
    name = input("Qual é o seu nome? ")
    message = input("Se pudesse visitar um lugar do mundo, para onde você "
                    "iria? ")
    responses[name] = message

    encerrar = input("Gostaria de encerrar a pesquisa? (y/n)")
    if encerrar == 'y':
        polling_active = False

for name, lugar in responses.items():
    print(name + ": " + lugar)