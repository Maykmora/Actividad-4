print("Bienvenido al programa")
users={"maynor":"mouse25", "juanito":"admin123", "carlos":"windows23"}

user=input("Ingrese su usuario:")
password=input("Ingrese su contraseña:")

if user in users and users[user]==password:
    print("Usuario y contraseña correcta, bienvenido al menu")
    print("1.Ver perfil")
    print("2.Cambiar contraseña")
    print("3.Cerrar sesión")

else:
    print("Usuario y contraseña incorrecta, intento 1 de 3")
    print()
    user = input("Ingrese su usuario:")
    password = input("Ingrese su contraseña:")

    if user in users and users[user] == password:
        print("Usuario y contraseña correcta, bienvenido al menu")
        print("1.Ver perfil")
        print("2.Cambiar contraseña")
        print("3.Cerrar sesión")

    else:
        print("Usuario y contraseña incorrecta, intento 2 de 3")
        print()
        user = input("Ingrese su usuario:")
        password = input("Ingrese su contraseña:")

        if user in users and users[user] == password:
            print("Usuario y contraseña correcta, bienvenido al menu")
            print("1.Ver perfil")
            print("2.Cambiar contraseña")
            print("3.Cerrar sesión")

        else:
            print("Usuario y contraseña incorrecta, ultimo intento")
            print()
            user = input("Ingrese su usuario:")
            password = input("Ingrese su contraseña:")

            if user in users and users[user] == password:
                print("Usuario y contraseña correcta, bienvenido al menu")
                print("1.Ver perfil")
                print("2.Cambiar contraseña")
                print("3.Cerrar sesión")

            else:
                print("Ya no te quedan intentos")
                print("Acceso bloqueado")


