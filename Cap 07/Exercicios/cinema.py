while True:
    message = input("Qual é a sua idade? ")

    if message == 'quit':
        break

    idade = int(message)
    if idade < 3:
        valor = 0
    elif idade <= 12:
        valor = 10
    elif idade > 12:
        valor = 15

    print("O ingresso vai custar " + str(valor))
