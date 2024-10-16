




"""
BUCLE INFINITO

while 10 > 5:
    print("SE CUMPLE")
"""

#CONTADOR--->FLAG


"""
contador = 0


while contador < 3:
    nombre_usuario = input("Ingrese su nombre")
    print(f"Bienvenido/a {nombre_usuario}")
    contador = contador + 1 

"""


#

"""
contador = 0

while contador <= 10:
    print(contador)
    contador = contador + 1
"""



#PEDIR UN NUMERO POR TECLADO Y MOSTRAR LA TABLA DEL MISMO

"""
contador = 0
numero = int(input("Ingrese un numero y le muestro la tabla del mismo"))

while contador <= 10:
    resultado = numero  * contador
    print(f"{numero} x {contador} = {resultado}")
    contador = contador + 1
"""



#Crear un programa que salue a X cantidad de usuarios
"""
nombre_usuario = ""


while nombre_usuario != "FIN":
    nombre_usuario = input("Ingrese su nombre | Ingrese FIN para terminar")
    if nombre_usuario != "FIN":
        print(f"Bienvenido/a {nombre_usuario}")
    else:
        print(f"Gracias por venir")
    
"""



#SE INGRESA UN NUMERO ENTERO POR TECLADO Y SE MUESTRA EL SIGUIENTE 
# HASTA QUE SE INGRESE UN NUMERO ENGATIVO

"""
num = 0

while num >= 0:
    num = int(input("Ingrese un numero positivo y le muestro el siguiente"))
    print(f"Ingreso: {num} el siguiente es: {num+1}")
"""



#SE INGRESAN NUMERO POR TECLADO MIESTRA LA SUMA TOTAL SEA MENOR A 500



acu = 0

while acu < 500:
    num = int(input("Ingrese un numero entero"))
    acu = acu + num
    print(f"Ingresaste: {num}")
    print(f"Suma total: {acu}")