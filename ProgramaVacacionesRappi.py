#Este en un programa de control de Vacaciones.
print ("""\n\n*|=================================|*
 |---PROGRAMA CONTROL VACACIONES---|
*|=================================|*\n\n"""
)

#Solicitar la clave del departamento
nombre = input("Por favor digite su nombre: ")
clave = int(input("""\n\n1: Clave1 <Departamento:Servicio al cliente>
2: Clave2 <Departamento:Logistica>
3: Clave1 <Departamento:Gerencia>\n
Por favor digite la Clave del departamento: """
))

#Solicitar los años
tiempo = int(input("\nPor digite la cantidad de años laborales: "))

#verificar si es clave 1
if clave == 1:
    print ("\nEs clave1")
    if tiempo == 1:
        print ("\nMensaje: 6 dias de vacaciones")
    elif tiempo >=2 and tiempo <=6:
        print ("\nMensaje: 14 dias de vacaciones")
    elif tiempo >= 7:
        print ("\nMensaje: 20 dias de vacaciones")
    else:
        print ("\nSin derecho a Vacaciones")  
elif clave == 2:
    print ("\nEs clave2")
elif clave == 3:
    print ("\nEs clave3")
else:
    print ("El dato no es correcto")