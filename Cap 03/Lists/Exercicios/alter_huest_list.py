convidados = ["Marisa", "Jarede", "Helena", "Mario"]

#Com laço
for i in convidados:
    print("Olá, " + i + " Tudo bem? \nConto com a sua presença!\n")

indisponível = convidados.pop(1);
print("O " + indisponível + " não vai comparecer. \n")

convidados.insert(1, "Joyce")

for i in convidados:
    print("Olá, " + i + " Tudo bem? \nConto com a sua presença!\n")