print ("Sistema para calcular promedio de un alumno.")
nombre = input("Para comenzar, ¿Cual es tu nombre?: ")
matematicas = float(input(nombre + "¿Cual es tu calificacion en matematicas?: "))
quimica = float(input(nombre + "¿Cual es tu calificacion en Quimica?: "))
biologia = float(input(nombre + "¿Cual es tu calificacion en biologia?: "))
promedio = (matematicas+quimica+biologia) / 3

if promedio >= 6:
    print ('Felicidades ' + nombre + ' "Aprobaste Crack"  Con un promedio: ',promedio)
    print ('Felicidades Crack ' + nombre + ' "Aprobaste"  Con un promedio: ',round (promedio,2))
elif promedio >= 5:
    print ('Puedes presentar ' + nombre + ' "Olimpiadas"  Con un promedio: ',promedio)
    print ('Puedes Presentar' + nombre + ' "Olimpiadas"  Con un promedio: ',round (promedio,2))
else:
    print ('Nombre: '+ nombre + ' "REPROBADO"  Con un promedio: ',promedio)
    print ('Nombre: '+ nombre + ' "REPROBADO"  Con un promedio: ',round (promedio,2))
    
print ("Fin.")
