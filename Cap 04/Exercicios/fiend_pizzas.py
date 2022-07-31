pizzas = ['Mussarela', 'Calabresa', 'Pepperoni', 'Palmito']

pizza_friend = pizzas[:]

pizzas.append('Lombo')

pizza_friend.append('Toscana')

print("Minhas pizzas favoritas são:")
for pizza in pizzas:
    print(pizza)

print("\nAs pizzas favoritas do meu amigo são:")
for pizza in pizza_friend:
    print(pizza)