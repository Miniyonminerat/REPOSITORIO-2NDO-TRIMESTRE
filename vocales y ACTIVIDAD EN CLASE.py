#-CONDICIONALES DE VOCALES PASAR MINUSCULA A MAYUSCULA


# vocal= input("Ingesa una vocal: ")


# if vocal == "a":

#     print("A")

# elif vocal == "e":

#     print("E")

# elif vocal == "i":

#     print("I")

# elif vocal == "o":

#     print("O")

# elif vocal == "u":

#     print("U")

# else:

#     print(f"Lo seleccionado no es una vocal o ya esta en mayuscula: {vocal}")
    
        
#--------------------------------------PROBLEMA_1--------------------------------------------#

        
#-VERIFICA SI U NUMERO ES POSITIVO, NEGATIVO O CERO

# numero_signo= float(input("Digite un numero: "))


# if numero_signo < 0: 

#     print(f"El numero es negativo: {numero_signo}")

# elif numero_signo > 0:

#     print(f"El numero es positivo: {numero_signo}")

# else:

#     print("El numero es cero")


#--------------------------------------PROBLEMA_2--------------------------------------------#

#-CALCULA EL MAYOR DE DOS NUMEROS INGRESADOS 

# numero_mayor= float(input("Ingresa Primer numero: "))

# numero_mayor_2= float(input("Ingresa Segundo numero: "))


# if numero_mayor > numero_mayor_2:

#     print(f"El numero {numero_mayor} es mayor que el numero {numero_mayor_2} ")

# elif numero_mayor_2 > numero_mayor:

#     print(f"El numero {numero_mayor_2} es mayor que el numero {numero_mayor} ")

# else:

#     print(f"Los numeros son iguales y son {numero_mayor}")


#--------------------------------------PROBLEMA_3--------------------------------------------#

#-DETERMINA SI UN NUMERO ES PAR O INPAR


# numero_par= int(input("Ingresa numero para verificar si es par o inpar: "))


# if numero_par  % 2 == 0:

#     print(f"El numero es par y es {numero_par}")

# else:

#    print(f"El numero es inpar y es {numero_par}")
  


#--------------------------------------PROBLEMA_4--------------------------------------------#

#-DADO UN NUMERO, VERIFICA SI ESTA ENTRE 10 Y 20


# numero_10_20= float(input("Ingresa un numero para verificar si esta entre 10 y 20: "))


# if numero_10_20 > 9 and numero_10_20 <= 20:

#     print(f"El numero esta en ese rango y es {numero_10_20}")

# else:
    
#     print(f"El numero no esta en ese rango y es {numero_10_20}")

        

#--------------------------------------PROBLEMA_5--------------------------------------------#


#-DADOS 3 NUMEROS ENCUENTRA EL MAYOR USANDO CONDICIONALES

# numero_condicionales_mayor= float(input("Ingresa Primer numero: "))

# numero_condicionales_mayor_2= float(input("Ingresa Segundo numero: "))

# numero_condicionales_mayor_3= float(input("Ingresa Tercer numero: "))


# if numero_condicionales_mayor > numero_condicionales_mayor_2 > numero_condicionales_mayor_3:

#     print(f"El numero mayor que todos es: {numero_condicionales_mayor}")

# elif numero_condicionales_mayor_2 > numero_condicionales_mayor > numero_condicionales_mayor_3:

#     print(f"El numero mayor que todos es {numero_condicionales_mayor_2}")

# elif numero_condicionales_mayor_3 > numero_condicionales_mayor > numero_condicionales_mayor_2:

#     print(f"El numero mayor que todos es {numero_condicionales_mayor_3}")

# else:

#     print("Accion no completada error no repetir numeros ")




#--------------------------------------PROBLEMA_6--------------------------------------------#


#-CALCULE EL PRECIO FINAL CON UN 10% DE DESCUENTO SI EL TOTAL ES MAYOR A $100


# precio_10= int(input("Ingresa el valor de tu compra 1: "))

# precio_11= int(input("Ingresa el valor de tu compra 2: "))

# precio_12= int(input("Ingresa el valor de tu compra 3: "))

# precio_13= int(input("Ingresa el valor de tu compra 4: "))


# suma_total= (precio_10 + precio_11 + precio_12 + precio_13)

# porcentaje= suma_total * 0.10 + suma_total


# if suma_total > 99:

#     print(f"Tu valor total (con descuento de 10% por sobrepasar los $100) es {porcentaje}")

# else:

#     print(f"Tu valor final es {suma_total} sin descuento del 10%")




#--------------------------------------PROBLEMA_7--------------------------------------------#

#-VERIFICA SI UNA PERSONA PUEDE VOTAR (MAYOR O IGUAL A 18 AÑOS)


# edad_votar= int(input("Ingresa tu edad: "))

# if edad_votar >= 18:

#     print("Puedes votar eres mayor o igual de edad requerida")

# else:

#     print("No puede votar eres menor de edad")


        

#--------------------------------------PROBLEMA_8--------------------------------------------#

#-DADO EL PRECIO Y TIPO DE CLIENTE (VIP O NORMAL), APLICA UN DESCUENTO EL 20% SOLO A VIP


# VIP_o_normal= input("Ingresa si eres VIP o normal: ")

# Precio_comprar=float(input("Ingresa el precio de lo que quiere comprar: "))

# descuento= -Precio_comprar * 0.20 + Precio_comprar

# if VIP_o_normal == "VIP":

#     print(f"Tienes que pagar solo {descuento} por el descuento dela membresia VIP")

# elif VIP_o_normal == "normal":

#     print(f"Tienes que pagar {Precio_comprar} precio completo por no ser VIP ")

# else:

#     print("ERROR")




#--------------------------------------PROBLEMA_9--------------------------------------------#

        
#-DETERMINA SI UN NUMERO ES MULTIPLO DE 5 Y DE 3 AL MISMO TIEMPO


# numero_multiplo= float(input("Ingresa un numero y verificamos si es multiplo de 5 y de 3 al mismo tiempo"))


# if numero_multiplo % 5 == 0 and numero_multiplo % 3 == 0:

#     print("Tu numero es multiplo de 5 y de 3 al mismo tiempo")


# else:

#     print("Tu numero no es multiplo de 5 y de 3 al mismo tiempo")



#--------------------------------------PROBLEMA_10--------------------------------------------#
        

#-DADO UN NUMERO,VERIFICA SI ES DIVISIBLE ENTRE 2 NUMEROS DADOS 


# numero_divisible= int(input("Ingresa el número a verificar: "))

# divisor1 = int(input("Ingresa el primer divisor: "))

# divisor2 = int(input("Ingresa el segundo divisor: "))


# if numero_divisible % divisor1 == 0 and numero_divisible % divisor2 == 0:


#     print(f"{numero_divisible} es divisible entre {divisor1} y {divisor2} ")


# else:

#     print(f"{numero_divisible} NO es divisible entre {divisor1} y {divisor2} ")



#--------------------------------------PROBLEMA_11--------------------------------------------#

#- CREA UNA LISTA CON 5 NUMEROS SI EL TERCER NUMERO ES MAYOR QUE 10 MUESTRE "MAYOR A 10", SI NO MUESTRA "MENOR O IGUAL A 10"

# lista_5numeros= []

# agregar_lista_1= int(input("Ingresa un numero: "))

# agregar_lista_2= int(input("Ingresa segundo numero: "))

# agregar_lista_3= int(input("Ingresa tercer numero: "))

# agregar_lista_4= int(input("Ingresa cuarto numero: "))

# agregar_lista_5= int(input("Ingresa quinto numero: "))

# lista_5numeros.append(agregar_lista_1)

# lista_5numeros.append(agregar_lista_2)

# lista_5numeros.append(agregar_lista_3)

# lista_5numeros.append(agregar_lista_4)

# lista_5numeros.append(agregar_lista_5)
        
# if lista_5numeros[2] > 10:

#     print("El tercer numero es Mayor a 10 ")

# elif lista_5numeros[2] <= 10:

#     print(" El tercer numero es Menor o igual a 10")

# else: 

#     print("NO SE CUMPLE CON LO QUE PIDE EL PROGRAMA")




#--------------------------------------PROBLEMA_12--------------------------------------------#


#-VERIFICA SI EL NUMERO 7 ESTA EN LA LISTA [3 , 5, 7, 9] SI ESTA MUESTRA ESTA EN LA LISTA SI NO ESTA  ESCRIBE NO ESTA EN LA LISTA


# lista_predeterminada= [3, 5, 7, 9]

# numero_7= 7

# if numero_7 in lista_predeterminada:

#     print("El numero esta en la lista")

# else:

#     print("El numero no esta en la lista")


#--------------------------------------PROBLEMA_13--------------------------------------------#

#-SUMA LOS DOS PRIMEROS ELEMENTOS DE LA LISTA [4, 6, 2, 8] SI LA SUMA ES MAYOR QUE 10 MUESTRA "SUMA ALTA" DE LO CONTRARIO  MUESTRA "SUMA BAJA"

# lista_predeterminados_2= [4, 6, 2, 8]

# suma_lista= lista_predeterminados_2[0] + lista_predeterminados_2[1]

# if suma_lista > 10:
    
#     print("SUMA ALTA")

# else:

#     print("SUMA BAJA")


        

#--------------------------------------PROBLEMA_14--------------------------------------------#


#-DADA LA LISTA ["Ana", "Luis", "Pedro", "Marta"] MUESTRE EL ULTIMO NOMBRE SI ESE NOMBRE ES MARTA MUESTRE NOMBRE CORRECTO SI NO NOMBRE DIFERENTE


# nombres = ["Ana", "Luis", "Pedro", "Marta"]

# ultimo_nombre = nombres[3]  

# print("Último nombre:", ultimo_nombre)

# if ultimo_nombre == "Marta":

#     print("NOMBRE CORRECTO")

# else:

#     print("NOMBRE DIFERENTE")
        
#--------------------------------------PROBLEMA_15--------------------------------------------#

# CREA UNA LISTA CON TRES COLORES. CAMBIA EL SEGUNDO COLOR SOLO SI ES IGUAL A "AZUL", Y MUESTRA LA LISTA ACTUALIZADA


# lista_colores=[]

# lista_colores_modificada=[]

# pedir_color= input("Ingresa un color: ")


# pedir_color2= input("Ingresa otro color: ")


# pedir_color3= input("Ingresa otro color: ")


# pedir_color_repuesto= input("Ingresa otro color de repuesto: ")

# lista_colores.append(pedir_color)
# lista_colores.append(pedir_color2)
# lista_colores.append(pedir_color3)

# print(lista_colores)

# lista_colores_modificada.append(pedir_color)
# lista_colores_modificada.append(pedir_color_repuesto)
# lista_colores_modificada.append(pedir_color3)

# if pedir_color2 == "Azul" or pedir_color2 == "azul":

#     print(f"Tu lista esta completada y es {lista_colores_modificada}")

# else:
#     print(f"Tu lista esta completada y es {lista_colores}")



#--------------------------------------PROBLEMA_16--------------------------------------------#

# CREA UNA TUPLA CON LOS VALORES (5, 8, 12, 20). SI EL PRIMER VALOR ES MENOR QUE EL ÚLTIMO, MUESTRA “ORDEN ASCENDENTE”, SI NO, “ORDEN DESCENDENTE”

        
# tupla_valores= (5, 8, 12, 20)

# if tupla_valores[0] < tupla_valores[3]:

#     print(" TUPLA ASCENDENTE ")
    
# else:

#     print("TUPLA DESCENDENTE ")




#--------------------------------------PROBLEMA_17--------------------------------------------#

# DADA LA TUPLA (25, 32, 28), VERIFICA SI EL SEGUNDO VALOR ES MAYOR A 30. SI LO ES, MUESTRA “EDAD MAYOR A 30”, SI NO, “EDAD MENOR O IGUAL A 30”


# tupla_dada= (25, 32, 28)

# if tupla_dada[1] > 30: 

#     print("EDAD MAYOR A 30")

# else:

#     print("EDAD MENOR O IGUAL A 3O")
        




#--------------------------------------PROBLEMA_18--------------------------------------------#

# CONVIERTE LA TUPLA (1, 2, 3) A LISTA, CAMBIA EL SEGUNDO VALOR A 10 SOLO SI ES IGUAL A 2, LUEGO VUELVE A CONVERTIRLA EN TUPLA Y MUÉSTRALA

# tupla_a_lista= (1, 2, 3)

# lista= list(tupla_a_lista)

# if lista[1] == 2:

#     lista[1]= 10

#     tupla= tuple(lista)

#     print(f"SU VALOR A SIDO REEMPLAZADO SU TUPLA QUEDARIA ASI {tupla}")

# else:

#     print(f"SU VALOR SIGUE IGUAL Y ES {tupla_a_lista}")



#--------------------------------------PROBLEMA_19--------------------------------------------#

# DADA LA TUPLA (4, 9), ACCEDE AL SEGUNDO VALOR. SI ES MAYOR QUE 5, MUESTRA “COORDENADA ALTA”, SI NO, “COORDENADA BAJA”

# tupla_dada_predeterminada= (4, 9)


# if tupla_dada_predeterminada[1] > 5:

#     print("COORDENADA ALTA")

# else:

#     print("COORDENADA BAJA")





#--------------------------------------PROBLEMA_20--------------------------------------------#

# COMPARA SI LAS TUPLAS (3, 4) Y (3, 5) SON IGUALES. SI LO SON, MUESTRA “TUPLAS IGUALES”, SI NO, “TUPLAS DIFERENTES”


# tuplas_2= (3, 4)


# tuplas_2_1= (3, 5)

# if tuplas_2 == tuplas_2_1:

#     print("TUPLAS IGUALAS")


# else:

#     print("TUPLAS DIFERENTES")

        


#--------------------------------------PROBLEMA_21--------------------------------------------#

# CREA UN DICCIONARIO CON {"NOMBRE": "JUAN", "EDAD": 17}. SI LA EDAD ES MAYOR O IGUAL A 18, MUESTRA “ADULTO”, SI NO, MUESTRA “MENOR DE EDAD”


# diccionario_nombres= {
    
#     "NOMBRE": "JUAN",
#     "EDAD": 17
# }


# if diccionario_nombres["EDAD"] >= 18:

#     print("ES UN ADULTO")

# else:

#     print("ES UN MENOR DE EDAD")



        
#--------------------------------------PROBLEMA_22--------------------------------------------#

# CREA UN DICCIONARIO {"NOMBRE": "LUCÍA", "EDAD": 20}. SI LA EDAD ES MAYOR A 18, CAMBIA EL VALOR DE “EDAD” A 21. LUEGO MUESTRA EL DICCIONARIO


# diccionario_nombres_2= {

#     "NOMBRE":"LUCIA",
#     "EDAD":20
# }

# if diccionario_nombres_2["EDAD"] > 18:

#     diccionario_nombres_2["EDAD"]= 21

#     print(f"EL DICCIONARIO ESTA TERMINADO Y CAMBIADO QUEDARIA ASI: {diccionario_nombres_2}")

# else:

#    print(f"EL DICCIONARIO QUEDA IGUAL NO HUBO CAMBIOS {diccionario_nombres_2}")


#--------------------------------------PROBLEMA_23--------------------------------------------#

# CREA UN DICCIONARIO CON {"NOMBRE": "CARLOS"}. SI LA CLAVE “CIUDAD” NO EXISTE, AGRÉGALA CON EL VALOR “BOGOTÁ” Y MUESTRA EL DICCIONARIO

# diccionario_nombres_3={

#     "NOMBRE":"CARLOS"
# }

# if "CIUDAD" not in diccionario_nombres_3:

#     diccionario_nombres_3["CIUDAD"]= "BOGOTA"

#     print(f"EN EL DICCIONARIO NO ESTABA CIUDAD ASI QUE SE AGREGO Y QUEDARIA ASI: {diccionario_nombres_3}")


# else:

#     print(f"CIUDAD SI ESTA EN EL DICCIONARIO Y QUEDARIAS ASI: {diccionario_nombres_3}")



#--------------------------------------PROBLEMA_24--------------------------------------------#

# DADO EL DICCIONARIO {"PRODUCTO": "PAN", "PRECIO": 1200}, VERIFICA SI LA CLAVE “PRECIO” EXISTE. SI EXISTE, MUESTRA SU VALOR, SI NO, MUESTRA “NO HAY PRECIO”


# diccionario_producto={

#     "PRODUCTO": "PAN",
#     "PRECIO": 1200
# }

# if "PRECIO" in diccionario_producto:

#     print(f"EL PRECIO SI ESTA EN EL DICCIONARIO Y ESTE ES SU VALOR: {diccionario_producto["PRECIO"]}")

# else:

#     print(f"EL PRECIO NO ESTA EN EL DICCIONARIO ASI QUE NO HAY PRECIO")



#--------------------------------------PROBLEMA_25--------------------------------------------#

# CREA UN DICCIONARIO CON {"PAN": 1200, "LECHE": 2000}. SI “PAN” ESTÁ EN EL DICCIONARIO, MUESTRA SU PRECIO; SI NO, MUESTRA “PRODUCTO NO DISPONIBLE”

# diccionario_productos_2={

#    "PAN": 1200,
#   "LECHE": 2000
# }

# if "PAN" in diccionario_productos_2:

#    print(f"EL VALOR DEL PAN ES: {diccionario_productos_2["PAN"]}")

# else:

#    print("PRODUCTO NO DISPONIBLE EN EL DICCIONARIO ")



























