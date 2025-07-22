weight=int(input("Ingrese el peso del paquete en kg:"))
distance=int(input("Ingrese la distancia en km:"))
urgency=input("¿Es de urgencia? (si/no):")
size=input("Ingrese el tamaño del paquete (pequeño/mediano/grande)")

if urgency=="no" and weight<5:
    print("Obtuviste un descuento de Q.20")

elif urgency=="si":
    print("Como el paquete es urgente tienes que pagar +Q.50")

elif weight=="grande":
    print("Como el paquete es urgente tienes que pagar +Q.30")

else:
    print("No tienes ningun recargo sobre tu paquete")
