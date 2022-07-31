sandwich_orders = ['pastrami', 'x-salada', 'x-tudo', 'x-egg', 'pastrami',
                   'pastrami']

message = "Não temos pastrami!\n"
print(message)

sandwich_orders.reverse()

finished_sandwiches = []

while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

    print("Preparei o seu sanduiche de " + sandwich_orders[-1].title())
    finished_sandwiches.append(sandwich_orders.pop())

print("\nSanduiches preparados: ")
for sandwich in finished_sandwiches:
    print("\t" + sandwich.title())