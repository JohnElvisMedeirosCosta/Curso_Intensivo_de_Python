rios = {
    'nilo' : 'egito',
    'amazonas' : 'brasil',
    'tamiza' : 'inglaterra',
    'tiete' : 'brasil'
}

for rio in rios.keys():
    print("O " + rio.title() + " percorre o " + rios[rio] + ".")
    
print("\n")
for rio in rios.keys():
    print(rio.title())

print("\n")
for rio in rios.keys():
    print(rios[rio].title())