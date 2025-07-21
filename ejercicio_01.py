print("Bienvenido al programa")
print()
name=input("Ingrese su nombre:").lower()
dpi=int(input("Ingrese su DPI:"))
department=input("Ingrese su departamento de origen:").lower()
year=int(input("Ingrese su año de nacimiento: "))

if year>2007:
    print("Puede votar")

if department == "petén" or department== "alta verapaz" and year==2008:
    print("Puede votar")