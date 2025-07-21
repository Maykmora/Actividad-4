price=1
prices=[]
tip1=0
discount=0
while price!=0:
    price=float(input("Ingrese el precio del producto o ingrese 0 para ya no agregar:"))
    prices.append(price)
    subtotal=sum(prices)

print("1.Agregar propina")
print("2.No agregar propina")
tip=int(input("Seleccione una opcion:"))
if tip==1:
    how=int("Escriba cual porcentaje quiere dejar de propina:")
    tip= subtotal*(how*1/100)
    print()
    print("1.Tiene tarejeta de cliente")
    print("2.No tiene tarjeta de cliente")
    card = int(input("Seleccione una opcion:"))
    if card == 1:
        print("Usted tiene el 10% de descuento")
        print()
        discount = subtotal * 0.10
        iva = subtotal * 0.12
        print(f"El subtotal es: {subtotal}")
        print(f"El iva agregado es: {iva}")
        print(f"El descuento es: {discount}")
        print(f"El total es:{subtotal + iva + discount}")

    else:
        print(f"El subtotal ")


else:
    print("1.Tiene tarejeta de cliente")
    print("2.No tiene tarjeta de cliente")
    card=int(input("Seleccione una opcion:"))
    if card==1:
        print("Usted tiene el 10% de descuento")
        print()
        discount=subtotal*0.10
        iva=subtotal*0.12
        print(f"El subtotal es: {subtotal}")
        print(f"El iva agregado es: {iva}")
        print(f"El descuento es: {discount}")
        print(f"El total es:{subtotal+iva+discount}")

    else:
        print()
