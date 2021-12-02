print("Ingrese el limite inferior: ")
limInf=int(input())
print("Ingrese el limite superior: ")
limSup=int(input())
print("Ingrese el numero a buscar en el rango: ")
num1=int(input())

if(num1>=limInf and num1<=limSup ):
    print("El numero " +str(num1) +" se encuentra dentro del limite.!!")
else:
    if(num1<limInf):
        print("El numero " +str(num1) +" se encuentra por debajo del limite inferior.")
    else:
        print("El numero " +str(num1) +" se encuentra por encima del limite superior.")