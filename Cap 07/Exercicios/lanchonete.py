sandwich_orders = ['bauru', 'x-salada', 'x-tudo', 'x-egg', 'hambuguer', 'atum']
sandwich_orders.reverse()

finished_sandwiches = []

while sandwich_orders:
    print("Preparei o seu sanduiche de " + sandwich_orders[-1].title())
    finished_sandwiches.append(sandwich_orders.pop())

print("\nSanduiches preparados: ")
for sandwich in finished_sandwiches:
    print("\t" + sandwich.title())