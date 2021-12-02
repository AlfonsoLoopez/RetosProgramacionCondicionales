confirmacion = True

while(confirmacion):
    print("Ingrese un numero entre el 1-6.")
    opcion=int(input())
    if opcion<1 or opcion>6:
        print("Opcion fuera de rango.")
    else:
        confirmacion = not confirmacion
if opcion ==1: print("Hoy aprenderemos sobre programación.")
if opcion ==2: print("¿Qué tal tomar un curso de marketing digital?")
if opcion ==3: print("Hoy es un gran día para comenzar a aprender de diseño")
if opcion ==4: print("¿Y si aprendemos algo de negocios online?")
if opcion ==5: print("Veamos un par de clases sobre producción audiovisual.")
if opcion ==6: print("Tal vez sea bueno desarrollar una habilidad blanda en Platzi")