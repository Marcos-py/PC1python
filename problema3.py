payasos=int(input("Ingrese número de payasos vendidos = "))
munecas=int(input("Ingrese número de muñecas vendidas = "))
#Pesos en gramos
Peso_payasos=112
Peso_munecas=75
unidad="gramos"
Peso_total=Peso_payasos*payasos+Peso_munecas*munecas
#print("El peso total del paquete que será enviado es = ",Peso_total)
print("El peso 10total del paquete que será enviado es = {}  {}".format(Peso_total,unidad))