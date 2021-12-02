print("Ingrese el numero de rango: ")
rango = int(input())
print("Ingrese el numero a buscar en el rango: ")
num1 = int(input())

if(num1<=rango):
    print("El numero " +str(num1) +" esta dentro del rango, gracias!!")
else:
    print("El numero " +str(num1) +" excede el limite permitido. ")