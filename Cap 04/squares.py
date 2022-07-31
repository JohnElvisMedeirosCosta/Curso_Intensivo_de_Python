#squares=[]
#for value in range(1,11):
#    squares.append(value**2)

#print(squares)

#Comprehensions
square=[value**2 for value in range(1,11)]
print(square)

digits = []
for value in range(0, 10):
    digits.append(value)

print(min(digits))
print(max(digits))
print(sum(digits))