precioproducto = float(input("ingrese el precio del producto:"))

def seleccion(precioproducto):
    if precioproducto > 500:
        descuento = precioproducto*0.1
        totaldesc = precioproducto - descuento
        print("se aplico el descuento al producto y es de:", descuento, "por tanto el total seria:", totaldesc)
    else:
        print("no se aplico el descuento al producto, por tanto el precio del producto es:", precioproducto)

seleccion(precioproducto)
