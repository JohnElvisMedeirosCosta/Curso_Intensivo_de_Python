my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy fiend's favorite foods are:")
for food in friend_foods:
    print(food)

# Change the lists
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy fiend's favorite foods are:")
for food in friend_foods:
    print(food)