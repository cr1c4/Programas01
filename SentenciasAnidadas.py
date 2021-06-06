print ("""========
"Conversor"
=========\n\n""")

print ("Menu de opciones: \n")
print ("Preciona 1 para convertir de numero a palabra.")
print ("Preciona 2 para convertir de palabra a numero. \n")

opcion = int(input("¿Cual es tu opcion deseada?: "))

if opcion == 1:
    print ("\nConversor de numero a palabra.\n")

    opcion_uno = int(input("¿Cual es el numero que deseas convertir a palabra?: "))

    if opcion_uno == 1:
        print("El numero es 'UNO'")
    elif opcion_uno == 2:
        print("El numero es 'DOS'")
    elif opcion_uno == 3:
        print("El numero es 'TRES'")
    elif opcion_uno == 4:
        print("El numero es 'CUATRO'")
    elif opcion_uno == 5:
        print("El numero es 'CINCO'")

    else:
        print ("El numero seleccionado no esta registrado")
    
elif opcion == 2:
    print ("\nConversor de palabra a numero.\n")

    opcion_dos = input("¿Cual es la palabra que deseas convertir a numero?: ")
    opcion_dos = opcion_dos.lower()

    if opcion_dos == "uno":
        print ("El numero es '1'")
    elif opcion_dos == "dos":
         print ("El numero es '2'")
    elif opcion_dos == "tres":
         print ("El numero es '3'")
    elif opcion_dos == "cuatro":
         print ("El numero es '4'")
    elif opcion_dos == "cinco":
         print ("El numero es '5'")
    else:
        print ("El numero seleccionado no esta registrado")
                 
else:
    print ("Opcion no disponible")

print("Fin.")
