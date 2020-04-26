colores=["verde","morado","amarillo","morado"]

print(colores.pop(2))

colores.insert(1,"rojo")
colores.append("marron")
colores.remove("verde")
print(colores.count("morado"))

for i in colores:
    print(i)

numeros=[1,2,3,4,5]

for n in numeros:
    print(n)

numeros.reverse()
for nr in numeros:
    print(nr)

persona={"name":"axel","lastname":"montenegro","age":"28"}

persona.pop("lastname")
persona.update({"phone":"2234982523"})
persona.update({"name":"nicolas"})

for key, values in persona.items():
    print(key," ",values)

numeros[4]=6

numeros.extend(colores)

for nc in numeros:
    print(nc)


lolPJ={"pj":"vi","rol":"jungla","masestria":"5"}

persona.update(lolPJ)

for p, l in persona.items():
    print(p," ", l)

print(len(colores))
print(len(persona))