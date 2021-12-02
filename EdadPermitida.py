print("Ingrese su edad:")
edad=int(input())

if edad<18:
    print("¿Sabes hacia dónde dirigir tu futuro? Seguro puedo ayudarte.")
else:
    if edad>=18 and edad<30:
        print("Es un momento excelente para impulsar tu carrera.")
    else:
        print("Nunca es tarde para aprender. ¿Qué curso tomaremos?")
