m1 =[
    [1,2,3],
    [7,8,9],
    [13,14,15]
]

m2 =[
    [4,5,6],
    [10,11,12],
    [16,17,18]
]

m3 =[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

#recorrer matriz + sumas de valores + agregar a m3
for rowPosition,values in enumerate(m1):# row = 0 values = [1,2,3]
    for colPosition, values2 in enumerate(values): #col = 0 in [1,2,3] values2=1
        m3[rowPosition][colPosition]= values2+m2[rowPosition][colPosition]

print(m3) 