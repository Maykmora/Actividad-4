print("Bienvenido al programa")
students=[]

for i in range(5):
    nombre=input(f"Nombre del estudiante {i+1}:")
    notas=[]
    for j in range(3):
        nota=float(input(f"Nota {j+1} de {nombre}:"))
        notas.append(nota)
    students.append({"nombre": nombre, "notas": notas})

promedios=[]
for estudiante in students:
    promedio = sum(estudiante["notas"]) / 3
    promedios.append(promedio)
