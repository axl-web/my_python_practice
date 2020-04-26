#Ejemplo sin map
numbers=[1,2,3,4,5]
update=[]

for value in numbers:
    update.append(value*2)

print(update)

#Ejemplo con map
def operation(value):
    return value*2

print(list(map(operation,numbers)))

#ejemplo con map y lambda
print(list(map((lambda value: value*2),numbers)))