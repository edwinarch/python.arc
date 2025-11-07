# Pide el ingreso anual y aplica impuestos segun:

ingr = float(input("Ingrese e;l primer NUM"))

if ingr < 10000:
    impuesto = ingr * 0.5

if ingr <= 20000:
    impuesto = ingr * 0.10
else:
    impuesto = ingr * 0.15

pago_neto = ingr - impuesto

print("pago neto anual son:", pago_neto)

#print("Hawo, world :3")
# Calcular el monto del impuesto y el pago neto anual.
