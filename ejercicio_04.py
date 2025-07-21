price=1
prices=[]
while price!=0:
    price=float(input("Ingrese el precio del producto o ingrese 0 para ya no agregar:"))
    prices.append(price)
    subtotal=sum(prices)
    print("1.Agregar propina")
    print("2.No agregar propina")
    tip=int(input("Seleccione una opcion:"))
