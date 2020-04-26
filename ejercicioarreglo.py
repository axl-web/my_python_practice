numeros=[1,2,3,4,5,6,7,8,9]


def suma (list):
    cuenta=0
    for value in list:
        cuenta = cuenta + value 
    return cuenta

print("la suma de la lista es: ",suma(numeros))


def parOin (list):
    par = 0
    inp = 0
    for value in list:
        if value % 2 == 0:
            par = par + value
            print(par)
        else:
            inp = inp + value
            print(inp)
    print("la suma de pares es: ",par )
    print("la suma de inpares es: ",inp )
    
parOin(numeros)

