current_users = ['john', 'carlos', 'marcelo', 'leticia', 'admin']
new_users = ['maria', 'CARLOS', 'marcelo', 'josé', 'antonio']

if new_users:
    for new_user in new_users:
        if new_user in current_users:
            print("Usuário " + new_user +" já existe")
        elif new_user.upper() in current_users:
            print("Usuário " + new_user + " já existe")
        elif new_user.lower() in current_users:
            print("Usuário " + new_user + " já existe")
        elif new_user.title() in current_users:
            print("Usuário " + new_user + " já existe")
        else:
            print("O usuário " + new_user + " está disponível!")