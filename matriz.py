#matriz con arreglos
shoes =[
    ["tenis1","tenis2","tenis3"],
    ["tenis4","tenis5","tenis6"],
    ["tenis7","tenis8","tenis9"]]

print(shoes[0][0])

#matriz con diccionarios
shoes2 =[
    {"nike":"tenis1","adidas":"tenis2","converse":"tenis3"},
    {"nike":"tenis4","adidas":"tenis5","converse":"tenis6"},
    {"nike":"tenis7","adidas":"tenis8","converse":"tenis9"}]

print(shoes2[1]["adidas"])

#matriz de diccionarios
shoes3 ={
   "nike":["tenis1","tenis2","tenis3"],
   "adidas":["tenis4","tenis5","tenis6"],
   "converse":["tenis7","tenis8","tenis9"]}

print(shoes3["converse"][2])

#recorer matriz de diccionarios

for key, lst in shoes3.items():
    for values in lst:
        print("estos son los sapato: ", key , values)
    
