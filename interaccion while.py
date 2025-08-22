# num = int(input("Ingrese un numero")) 

# while num > 0:  

#     print(f"{num}")  

#     num -= 1

#     print("Termino el conteo") 

#----------------------------------ejemplo 2 ------------------------------#


# numero = int(input("Ingresa numero de la tabla de multiplicar"))


# i = 1 

# print(f"\n inicia el contador en el 1 {numero}: ")

# while i <= 10:

#     print(f"{numero} * {i} = {numero * i}")

#     i += 1


#----------------------------------ejemplo 3 (practica) ------------------------------#

#- haz un programa que le pida al usuario un numero y sume todos los numeros que ingrese, hasta que escriba 0


# #-inicializamos operacion (suma)

# suma_total= 0

# #-pedimos el numero 

# numero_usuario = int(input("Ingrese numero usuario: "))



# while numero_usuario != 0:

#     suma_total += numero_usuario #- suma total

#     numero_usuario_2 = int(input("Ingrese el numero 0 para salir del bucle")) #-Para acabar bucle

#     print("La suma total es :" , suma_total) #-total

    
#- al salir o ingresar el numero 0 se va a sumar y sumar y sumar siempre que coloquemos el cero
    



#----------------------------------ejemplo 4 break ------------------------------#


# x= 5
# while True:
#     x -= 1  #- se le resta 1 al 5 

#     print(x) #- se imprime el valor restado

#     if x == 0: #- si x es igual a 0 romper el bucle se acaba en 0 si no sigue el bucle 
#         break
#     print("Fin del bucle")




#----------------------------------ejercicio 1 ------------------------------#



# suma_total= 0
# contador = 1

 
# while contador <= 5:
#     numero_usuario = int(input(f"Ingrese el número {contador} (0 para terminar): "))


#     if numero_usuario == 0:
#         break

#     suma_total += numero_usuario

#     contador += 1

#     print("La suma total es :" , suma_total) 


#----------------------------------ejercicio 2   ------------------------------#

contraseña= input("Ingresa tu contraseña: ")

while contraseña != "python123":

    print("CONTRASEÑA INCORRECTA")

    if contraseña == "python123":

        print("CONTRASEÑA CORRECTA")


    contraseña= input("Ingresa tu contraseña: ")

    
    

















































































