
# primer letra en mayuscula y el resto en minuscula
txt= "hola mundo."
x= txt.capitalize()
print(x)

# prime letra en mayuscula y el resto en minuscula, pero no cambia las mayusculas porque es numero
txt= "27 es mi edad."
x= txt.capitalize()
print(x)

# lo que estan en mayusculas se convierte a minusculas
txt= "Hola mis AMIGOS"
x= txt.lower()
print(x)

# lo que estan en minusculas se convierte a mayusculas, y, # lo que estan en mayusculas se convierte a minusculas
# se pone reversa
txt= "Hola mi nombre es Ariel"
x= txt.swapcase()
print(x)