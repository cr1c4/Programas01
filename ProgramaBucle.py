x,y=0,1
while x <= 1597:
    print (x,y,end=" ")
    x=x+y
    y=x+y
print ("Fin")

import os

#Programa para calcular el valor de PI
k,r=0,0
while True:
    r += 4 * pow(-1, k) / (2 * k + 1)
    k += 1
    os.system("Clear")
    print (k)
    print (r)