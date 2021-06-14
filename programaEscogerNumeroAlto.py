#Programa para determinar si el numero es Par o Impar.
print ("""\n\n*|=================================|*
 |---PROGRAMA ESCOGER EL NUMERO MAS ALTO---|
*|=================================|*\n\n"""
)

#Solicitar numeros enteros 
numeroEntero1 = int(input("Introduce el primer numero: "))
numeroEntero2 = int(input("Introduce el segundo numero: "))
numeroEntero3 = int(input("Introduce el tercer numero: "))

if numeroEntero1 > numeroEntero2 and numeroEntero1 >numeroEntero3:
    print ("El numero ",numeroEntero1," es el numero mas grande de los 3.")
else:
    if numeroEntero2 > numeroEntero3:
        print ("El numero ",numeroEntero2," es el numero mas grande de los 3.")
    else:
       print ("El numero ",numeroEntero3," es el numero mas grande de los 3.") 
