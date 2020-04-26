def validacion(message):
    while True:
        try:
            dato = float(input("Ingresa " + message))
            return dato     
        except ValueError:
            print("El dato debe ser un numero entero o decimal")


largo =validacion("el largo en metros: ")
ancho =validacion("el ancho en metros: ")
m2xCaja =validacion("los metros cuadrados por caja: ")
precioxm2 =validacion("el precio por metro cuadrado: ")

precioxCaja=(m2xCaja * precioxm2)
m2Cuarto = largo * ancho
cajas = m2Cuarto/m2xCaja
precioTotal = cajas * precioxCaja

print("total de cajas que se necesitan:", cajas)
print("Precio total: ","$",precioTotal)     

