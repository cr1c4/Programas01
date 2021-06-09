#Programa para determinar si el numero es Par o Impar.
print ("""\n\n*|=================================|*
 |---PROGRAMA PAR & IMPAR---|
*|=================================|*\n\n"""
)

#Solicitar el numero entero
numeroEntero = int(input("Por favor introducir un numero entero: "
))

if numeroEntero % 2 == 0:
    print ("El numero ",numeroEntero," es par.")
elif numeroEntero % 2 == 1:
    print ("El numero ",numeroEntero," es impar.")

