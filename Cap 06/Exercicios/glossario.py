glossario = {
    'Programar' : 'Ato de desenvolver algo.',
    'Escrever' : 'Bla bla bla bla',
    'Falar' : 'blu blu blu',
    'Chorar' : 'Nhe nhe nhe'
}

for key, value in glossario.items():
    print(key, ": \n" + value + "\n")

glossario['Estudo'] = 'Forma abc'
glossario['Teste'] = 'Testar algo.'
glossario['Escola'] = 'Ambiente de estudo'
glossario['Computador'] = 'Meu vicio'
glossario['Teclado'] = 'Ferramenta de input do computador'

for name in glossario.keys():
    print(name, ": \n" + glossario[name] + "\n")