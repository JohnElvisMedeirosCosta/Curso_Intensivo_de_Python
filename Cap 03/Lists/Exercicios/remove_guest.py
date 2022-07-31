convidados = ["Marisa", "Jarede", "Helena", "Mario"]

#Com laço
for i in convidados:
    print("Olá, " + i + " Tudo bem? \nConto com a sua presença!\n")

indisponível = convidados.pop(1);
print("O " + indisponível + " não vai comparecer. \n")

convidados.insert(1, "Joyce")

for i in convidados:
    print("Olá, " + i + " Tudo bem? \nConto com a sua presença!\n")

for i in convidados:
    print(i + ", encontrei uma mesa maior e teremos mais convidados!")

convidados.insert(0, "Maria")
convidados.insert(3, "José")
convidados.append("Laura")

for i in convidados:
    print("Olá, " + i + " Tudo bem? \nConto com a sua presença!\n")

print("Infelizmente a mesa não vai chegar a tempo e só posso ter dois convidados!")

print(convidados)

for i, name in enumerate(convidados[:]):
    if i != 0 and i != 1:
        print("Me desculpe " + name)
        convidados.remove(name)

#removed = convidados.pop(2)
#print("Me desculpe " + removed)

#removed = convidados.pop(2)
#print("Me desculpe " + removed)

#removed = convidados.pop(2)
#print("Me desculpe " + removed)

#removed = convidados.pop(2)
#print("Me desculpe " + removed)

#removed = convidados.pop(2)
#print("Me desculpe " + removed)

#for i in convidados:
#   print("\n" + i + " você continua na lista!")

del convidados[0]
del convidados[0]
print(convidados)