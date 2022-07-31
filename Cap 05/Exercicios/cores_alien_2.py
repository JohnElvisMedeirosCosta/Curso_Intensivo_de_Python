alien_color = 'green'

if alien_color == 'green':
    pontos = 5
else:
    pontos = 10

if pontos >= 0:
    message = ' ganhou '
else:
    message = ' perdeu '

print( "Você" + message + str(pontos) + " pontos.")

#----------------------------------------------------------------------------

alien_color = 'red'

if alien_color == 'green':
    pontos = 5
else:
    pontos = 10

if pontos >= 0:
    message = ' ganhou '
else:
    message = ' perdeu '

print("Você" + message + str(pontos) + " pontos.")
