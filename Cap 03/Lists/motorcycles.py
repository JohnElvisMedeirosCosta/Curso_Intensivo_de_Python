motorcycles = ['honda', 'yamaha', 'suziki']

print(motorcycles)

#substituindo o elemento da posição 0
#motorcycles[0] = 'ducati'
#print(motorcycles)

#concatenando um novo elemento na lista
motorcycles.append('ducati')
print(motorcycles)
      
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suziki')

print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suziki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suziki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

#O método pop remove o valor da lista, porém adiciona ele em outra variável
motorcycles = ['honda', 'yamaha', 'suziki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suziki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

#removendo o item de acordo com o seu valor
motorcycles = ['honda', 'yamaha', 'suziki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suziki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")