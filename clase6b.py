

#STRINGS

nombre = "Juan"


#ACCESO

print( nombre[0] )


#LARGO DEL STRING

print( len(nombre) )


#

#nombre[0] = "R" OJO



#SLICING

frase = "Los perros son buenos y los gatos tambien"

print( frase[2])
print( frase[24:])


#METODOS

#Upper

print( frase.upper() )


#Lower

print( frase.lower())



#ITERABLE



cadena = "Talento Tech"

# Inicializamos el contador para los índices
indice = 0

# Usamos un bucle while para recorrer la cadena
while indice < len(cadena):
   # Mostramos el número y el carácter
   print("caracter", indice + 1, ":", cadena[indice])
  
   # Incrementamos el contador en 1
   indice = indice + 1