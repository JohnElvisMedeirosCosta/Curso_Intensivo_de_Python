users = ['john', 'carlos', 'marcelo', 'leticia', 'admin']

if users:
    for user in users:
        if user == 'admin':
            print("Olá admin, gostaria de ver um relatório de status?")
        else:
            print("Olá " + user + ", obrigado por fazer login novamente.")
else:
    "Lista vazia"