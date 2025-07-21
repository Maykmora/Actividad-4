print("Bienvenido al programa")
print()
name=input("Ingrese su nombre:").lower()
dpi=int(input("Ingrese su DPI:"))
department=input("Ingrese su departamento de origen:").lower()
year=int(input("Ingrese su año de nacimiento: "))

if year>2007:
    print("No puedes votar porque eres menor de edad")

elif department == "petén" or department== "alta verapaz" and year<2008:
    print(f"Puede votar porque es de {department} y tiene 17 años o menos")
    print(f"Bienvenido {name}, su centro de votación esta en {department}")

elif len(name)<5 or len(str(dpi))<13 or len(str(dpi))>13:
    print("No puedes votar porque tu nombre tiene menos de 5 letras o no ingresaste correctamente el dpi")