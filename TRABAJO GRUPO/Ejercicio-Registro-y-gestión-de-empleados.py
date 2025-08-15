# Ejercicio Registro y Gestión de Empleados #

numero_de_empleados = int(input("Ingrese la cantidad de empleados a registrar (1-5): "))

empleados = []
if numero_de_empleados < 1 or numero_de_empleados > 5:

    print("EL NUMERO DE EMPELADOS O SOBRE PASA LA CANTIDAD REQUERIDA O ES MENOR A 1 ")



# Empleado 1 
if numero_de_empleados >= 1: 
    nombre1 = input("ingresa el nombre del empleado 1: ")
    cargo1 = input("ingresa el cargo del empleado 1: ")
    salario_bruto1 = float(input("ingresa el salario bruto mensual del empleado 1: "))
    salud1 =  salario_bruto1 * 0.04
    pension1 = salario_bruto1 * 0.04
    salario_neto1 = salario_bruto1 - (salud1 + pension1)

    empleado1 = {
        "nombre": nombre1,
        "cargo": cargo1,
        "salario_bruto": salario_bruto1,
        "salud": salud1,
        "pension": pension1,
        "salario_neto": salario_neto1
    }
    empleados.append(empleado1)

# Empleado 2
if numero_de_empleados >= 2: 
    nombre2 = input("ingresa el nombre del empleado 2: ")
    cargo2 = input("ingresa el cargo del empleado 2: ")
    salario_bruto2 = float(input("ingresa el salario bruto mensual del empleado 2: "))
    salud2 =  salario_bruto2 * 0.04
    pension2 = salario_bruto2 * 0.04
    salario_neto2 = salario_bruto2 - (salud2 + pension2)
    
    empleado2 = {
        "nombre": nombre2,
        "cargo": cargo2,
        "salario_bruto": salario_bruto2,
        "salud": salud2,
        "pension": pension2,
        "salario_neto": salario_neto2
    }
    empleados.append(empleado2)

# Empleado 3
if numero_de_empleados >= 3: 
    nombre3 = input("ingresa el nombre del empleado 3: ")
    cargo3 = input("ingresa el cargo del empleado 3: ")
    salario_bruto3 = float(input("ingresa el salario bruto mensual del empleado 3: "))
    salud3 =  salario_bruto3 * 0.04
    pension3 = salario_bruto3 * 0.04
    salario_neto3 = salario_bruto3 - (salud3 + pension3)
    
    empleado3 = {
        "nombre": nombre3,
        "cargo": cargo3,
        "salario_bruto": salario_bruto3,
        "salud": salud3,
        "pension": pension3,
        "salario_neto": salario_neto3
    }
    empleados.append(empleado3)

# Empleado 4
if numero_de_empleados >= 4: 
    nombre4 = input("ingresa el nombre del empleado 4: ")
    cargo4 = input("ingresa el cargo del empleado 4: ")
    salario_bruto4 = float(input("ingresa el salario bruto mensual del empleado 4: "))
    salud4 =  salario_bruto4 * 0.04
    pension4 = salario_bruto4 * 0.04
    salario_neto4 = salario_bruto4 - (salud4 + pension4)
    
    empleado4 = {
        "nombre": nombre4,
        "cargo": cargo4,
        "salario_bruto": salario_bruto4,
        "salud": salud4,
        "pension": pension4,
        "salario_neto": salario_neto4
    }
    empleados.append(empleado4)

# Empleado 5
if numero_de_empleados >= 5: 
    nombre5 = input("ingresa el nombre del empleado 5: ")
    cargo5 = input("ingresa el cargo del empleado 5: ")
    salario_bruto5 = float(input("ingresa el salario bruto mensual del empleado 5: "))
    salud5 =  salario_bruto5 * 0.04
    pension5 = salario_bruto5 * 0.04
    salario_neto5 = salario_bruto5 - (salud5 + pension5)
    
    empleado5 = {
        "nombre": nombre5,
        "cargo": cargo5,
        "salario_bruto": salario_bruto5,
        "salud": salud5,
        "pension": pension5,
        "salario_neto": salario_neto5
    }
    empleados.append(empleado5)

# Resumen  
print("Resumen de empleados")

if numero_de_empleados >= 1:
    print("| Nombre:", empleados[0]["nombre"], "| Cargo:", empleados[0]["cargo"], "| Salario neto:", empleados[0]["salario_neto"])
if numero_de_empleados >= 2:
    print("| Nombre:", empleados[1]["nombre"], "| Cargo:", empleados[1]["cargo"], "| Salario neto:", empleados[1]["salario_neto"])
if numero_de_empleados >= 3:
    print("| Nombre:", empleados[2]["nombre"], "| Cargo:", empleados[2]["cargo"], "| Salario neto:", empleados[2]["salario_neto"])
if numero_de_empleados >= 4:
    print("| Nombre:", empleados[3]["nombre"], "| Cargo:", empleados[3]["cargo"], "| Salario neto:", empleados[3]["salario_neto"])
if numero_de_empleados >= 5:
    print("| Nombre:", empleados[4]["nombre"], "| Cargo:", empleados[4]["cargo"], "| Salario neto:", empleados[4]["salario_neto"])

else:

    print("CANTIDAD ERRONEA")


print("FIN")