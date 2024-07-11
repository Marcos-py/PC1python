#Ingresar datos coherentes: 0 <= HH < 24 y 0 <= MM < 60
hora_ingresada = input("Ingrese la hora en el siguiente formato (HH:MM): ")
#convertir string en datos numericos
horas, minutos = hora_ingresada.split(':')
horas = int(horas)
minutos = int(minutos)
#Asignamos a la variable X el tiempo en minutos
X=(horas * 60 + minutos)
#print(X)
#Rango de 07:00 a 08:00 en minutos
if X>=420 and X<=480:
    print("Es la hora del desayuno")
#Rango de 12:00 a 13:00 en minutos
elif X>=720 and X<=780:
    print("Es la hora del almuerzo")
#Rango de 18:00 a 19:00 en minutos
elif X>=1080 and X<=1140:
    print("Es la hora de la cena")
#Tiempo fuera de los rangos anteriores
else:
    print("No es la hora de alimentarse")