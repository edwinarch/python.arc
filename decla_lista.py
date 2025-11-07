
#correos= ["Gmail","Hotmail","Yahoo" ]
#print(correos[2])

#c= len(correos)
#print(c)

\
\
\

# el print leer correos[2] y muestra el tercer elemento de la lista
# el len(correos) devuelve la cantidad de elementos en la lista
## el append agrega un nuevo elemento al final de la lista
# el pop elimina el elemento en la posición indicada (en este caso, el tercer elemento)
correos= ["Gmail","Hotmail","Yahoo" ]
print(correos[2])

cantidad= len(correos)
print(cantidad)

#agregar un nuevo correo
correos.append("Outlook")
print(correos)

# el pop y más (2) es como agregar otro correos asi....
correos.pop(2)
print(correos)

correos.remove("Gmail")
print(correos)



