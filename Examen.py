#Python que simule el comportamiento de un cajero automático dicho software debe de realizar las siguientes 

import os


retirar = 0
i3 = 1



saldo = 0

print ("Bienvenido al sistema Banco BCR")
clave = "1980"
usuario = "Darian"
i2 = input("Introduce el usuario: ")
i = input("Digite la clave: ")
contador = 1
while clave.lower() != i and usuario != i2  and contador <= 3:
    print (f"El usario y la contraseña no es correcta le quedan {3 - contador} intentos")
    contador+=1
    

    i2 = input('Introduzca de nuevo el usario : ')
    i = input ("Introduzca de nuevo la contrasena: ")

while i3 == 1 and contador <= 3:
    print("1 = Deseo ingresar dinero ")
    print("2 = Deseo retirar dinero")
    print("3 = Deseo mirar mi dinero disponible")
    print("4 = Salir")
    option = int(input("Digite una acción del menu: "))
    print ("_________________________________________")
    if (option == 1):
        ex = float(input("Cuanto dinero desea ingresar: "))
        saldo += ex
        print ("El saldo actual de tu cuenta es:",saldo,"₡")
    elif(option == 2):
        retirar = float(input("Cuánto dinero desea retirar?: "))
        if (saldo < retirar):
            print("No hay fondos disponibles")
        else:
            saldo -= retirar 
            print("Los fondos disponibles son:",saldo,"₡")
    elif (option == 3):
        print("Tu saldo es:",saldo,"₡")
    elif (option == 4):
        print("Gracias por tu tiempo")
        exit()
    else:
        print("Error, ingrese una opción valida")
    respuesta = input("¿Desea realizar otra operación? SI / NO ")
    if (respuesta == "s" or respuesta == "si" or respuesta == "S" or respuesta == "SI" or respuesta == "SÍ" or respuesta == "sí"):
        i3 = 1
    else:
        i3 = 0
        print("Gracias por utilizar los servicios del BCR.")
        print("Retire su tarjeta")
else:
    contador == 3
    print(" SE HA BLOQUEADO LA TARJETA ")