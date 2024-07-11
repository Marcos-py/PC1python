num1=int(input("Ingrese un número = "))
num2=int(input("Ingrese otro número = "))
suma=num1+num2
resta=num1-num2
multi=num1*num2
#Seleccione una opción
opcion=int(input("Digitar una opción: 1 para suma, 2 para resta, 3 para multiplicación: "))
if opcion==1:
    print("La suma es = ",suma)
elif opcion==2:
    print("La resta es = ",resta)
elif opcion==3:
    print("La multiplicación es = ",multi)
else:
    print("Opción no válida")