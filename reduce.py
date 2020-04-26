import functools# acticacion de reduce en functools
#ejemplo sin reduce
numeros = [1,2,3,4,5,6,7,8,9]
result = 0

for n in numeros:
    result = result +n

print(result)
#ejemplo con reduce
print(str(functools.reduce((lambda x,y:x+y),numeros)))