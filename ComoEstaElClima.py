print("El dia de hoy esta lloviendo?")
lluvia = input()
lluvia = lluvia.upper()

if(lluvia == "SI" or lluvia =="SÍ"):
    print("Esta haciendo mucho viento?")
    viento = input()
    viento = viento.upper()
    if(viento == "SI" or viento =="SÍ"):
        print("Hace mucho viento para utilizar sombrilla.")
    else:
        print("Deberias utilizar una sombrilla.")
else:
    print("Tenga un bonito día.")