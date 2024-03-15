print("Bienvenido a cajero BI")

while True:
    print("1. Iniciar retiro")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Ingrese su identificación de usuario:")
        intentos = 3
        while intentos > 0:
            usuario = input("Usuario: ")
            if usuario == "Bcc-2215":
                print("Identificación de usuario correcta.")
                print("Ingrese su pin para continuar:")
                intentos_pin = 3
                while intentos_pin > 0:
                    pin = input("PIN: ")
                    if pin == "225125":
                        print("PIN correcto.")
                        while True:
                            print("Ingrese el monto a retirar:")
                            monto = int(input("Q "))
                            if monto % 5 == 0 and monto <= 3000:
                                print("Transacción realizada: Q", monto, ".00")
                                break
                            elif monto > 3000:
                                print("El monto excede el límite de Q 3000. Intente nuevamente.")
                            else:
                                print("El monto ingresado no es válido. Intente nuevamente.")
                        break
                    else:
                        print("PIN incorrecto. Inténtelo nuevamente.")
                        intentos_pin -= 1
                        if intentos_pin == 0:
                            print("Ha excedido el número de intentos. Por favor, vuelva a intentarlo.")
                            break
                break
            else:
                print("Identificación de usuario incorrecta. Por favor, inténtelo nuevamente.")
                intentos -= 1
                if intentos == 0:
                    print("Ha excedido el número de intentos. Por favor, vuelva a intentarlo.")
                    break
    elif opcion == "2":
        continue
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
