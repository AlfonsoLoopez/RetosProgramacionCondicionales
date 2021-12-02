##Obteniendo los numeros ingresados por el usuario.
print("Ingrese el primer numero: ")
num1 =int(input())
print("Ingrese el segundo numero: ")
num2= int(input())
may = num1
##Aplicando condicionales.
if(may>num2):
    print("El numero mayor es: " +str(may))
    print("Con una diferencia de " +str((may-num2)))
else:
    if(may==num2):
        print("Los numeros son iguales.")
        print("No existe diferencia.")
    else:
        may=num2
        print("El numero mayor es: " +str(may))
        print("Con una diferencia de: " +str((may-num1)))

