#Este en un programa de control.
print ("""\n\n*|=================================|*
 |---PROGRAMA CONTROL VACACIONES---|
*|=================================|*\n\n"""
)

#Solicitar la clave del departamento
clave = int(input("""\n\n1: Clave1 <Departamento:Servicio al cliente>
2: Clave2 <Departamento:Logistica>
3: Clave1 <Departamento:Gerencia>\n
Por favor digite la Clave del departamento: """
))



#Solicitar datos
nombre = input("\nPor favor digite su nombre: ")
tiempo = int(input("\nPor digite la cantidad de años laborales: "))

#verificar si es clave 1
if clave == 1:
    if tiempo == 1:
        DatoVacaciones = "\n6 dias"
    elif tiempo >=2 and tiempo <=6:
        DatoVacaciones = "\n14 dias"
    elif tiempo >= 7:
        DatoVacaciones = "\n20 dias"
    else:
        DatoVacaciones = "\nSin derecho a vacaciones"  
elif clave == 2:
    if tiempo == 1:
        DatoVacaciones = "7 dias"
    elif tiempo >=2 and tiempo <=6:
        DatoVacaciones = "15 dias"
    elif tiempo >= 7:
        DatoVacaciones = "22 dias"
    else:
        DatoVacaciones = "Sin derecho a vacaciones"  
elif clave == 3:
    if tiempo == 1:
        DatoVacaciones = "10 dias"
    elif tiempo >=2 and tiempo <=6:
        DatoVacaciones = "20 dias"
    elif tiempo >= 7:
        DatoVacaciones = "30 dias"
    else:
        DatoVacaciones = "Sin derecho a vacaciones"
else:
    print ("\nEl valor de departamento no es correcto")

if clave == 1 or clave == 3 or clave == 3:
    print ("\n\n============Resultados============\nEmpleado: ",nombre)
    print ("Antiguedad: ",tiempo," años")
    print ("Vacaciones disponibles por: ",DatoVacaciones,"\n\n")

   
