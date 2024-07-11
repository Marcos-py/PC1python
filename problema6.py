#Preguntar al cliente su edad
edad=int(input("Ingrese su edad: "))
if edad<4:
    print("puede entrar gratis")
elif 4<=edad<=18:
    print("debe pagar 5")
else:
    print("debe pagar 10")     
#fin del progrma