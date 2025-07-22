print("Bienvenido al programa")
print()
coor1=input("Ingrese la primer cordenada:").lower()
coor2=input("Ingrese la segunda coordenada:").lower()

if coor1 == "norte" and coor2 == "este":
    print("Se movera en dirección a Noreste")
elif coor1 == "norte" and coor2 == "oeste":
    print("Se movera en dirección al noroeste")
elif coor1 == "sur" and coor2 == "este":
    print("Se movera en direccion al sureste")
elif coor1 == "sur" and coor2 == "oeste":
    print("Se movera en direccion al suroeste")
elif coor2 == "norte" and coor1 == "este":
    print("Se movera en dirección a Noreste")
elif coor2 == "norte" and coor1 == "oeste":
    print("Se movera en dirección al noroeste")
elif coor2 == "sur" and coor1 == "este":
    print("Se movera en direccion al sureste")
elif coor2 == "sur" and coor1 == "oeste":
    print("Se movera en direccion al suroeste")

else:
    print("La dirección no existe")