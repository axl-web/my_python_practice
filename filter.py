#Ejempli sin filter
numbers =[1,2,3,4,5,6]
even=[]

for value in numbers:
    if(value % 2 == 0):
        even.append(value)
print(even)

#ejemplo con filter
def ifEven(value):
    return value % 2 ==0

even=list(filter(ifEven,numbers))
print(even)

#ejemplo con filter y lambda
print(list(filter((lambda numbers:numbers % 2 == 0),numbers)))