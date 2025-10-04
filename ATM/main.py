import login

def consultar_saldo():
    print(f"Tu saldo actual es de: ")
    print(f"${login.saldo}")

def depositar_dinero(cantidad):
    if cantidad < 0:
        print("Tiene que ser una cantidad postiva!")
    else:
        login.saldo += cantidad
        login.cuentas[login.usuario]["saldo"] = login.saldo
        print("DEPOSITO EXITOSO")
        print("Tu saldo actual ahora es de:")
        print(f"${login.saldo}")
        login.cuentas[login.usuario]["historial"].append(("Deposito", cantidad, "3 Oct"))

def retirar_dinero(cantidad):
    if cantidad > login.saldo:
        print("Fondos Insuficientes!")
    else:
        login.saldo -= cantidad
        login.cuentas[login.usuario]["saldo"] = login.saldo
        print("RETIRO EXITOSO")
        print("Tu saldo actual ahora es de:")
        print(f"${login.saldo}")
        login.cuentas[login.usuario]["historial"].append(("Retiro", cantidad, "3 Oct"))

def transferir_dinero(cuenta, cantidad):
    if cuenta == login.usuario:
        print("Accion Invalida. Debes poner otra cuenta valida")
    elif not cuenta in login.cuentas.keys():
        print(f"{cuenta} no existe. Verifica el No. cuenta")
    elif cantidad > login.saldo:
        print("Saldo insuficiente para poder transferir")
    else:
        login.cuentas[cuenta]["saldo"] += cantidad
        login.saldo -= cantidad
        login.cuentas[login.usuario]["saldo"] = login.saldo
        print("TRANSFERENCIA EXITOSA!")
        print("Tu saldo actual ahora es de: ")
        print(f"${login.saldo}")
        login.cuentas[login.usuario]["historial"].append((f"Transferencia a {cuenta}", cantidad, "3 Oct"))

def ver_historial():
    if login.historial == []:
        print("No tienes movimientos")
    else:
        movimientos = 1
        for tipo, cantidad, fecha in login.cuentas[login.usuario]["historial"]:
            print(f"Movimientos : {movimientos}")
            print(f"Movimieto: {tipo}")
            print(f"Cantidad: ${cantidad}")
            print(f"Fecha: {fecha}")
            movimientos += 1

def cambiar_pin():
    pin_actual = input("Ingresa tu pin actual: ")

    if pin_actual == login.pin:
        pin_nuevo = input("Ingresa el PIN nuevo de 4 digitos: ")
        if len(pin_nuevo) < 4 or len(pin_nuevo) > 4:
            print("PIN invalido. Tiene que ser exactamente 4 digitos")
        else:
            login.cuentas[login.usuario]["pin"] = pin_nuevo
            print("CAMBIO DE PIN EXITOSO")
    else:
        print("PIN Incorrecto!") 


if __name__ == '__main__':
    
    while login.cajero_acceso:
        print("BIENVENIDO A TU ATM")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Transferir dinero")
        print("5. Ver historial de transacciones")
        print("6. Cambiar de PIN")
        print("7. Cerrar Sesion")
        print("8. Salir")

        opcion = input("Ingresa una opcion: ")

        if opcion == "1":
            consultar_saldo()

        elif opcion == "2":
            cantidad = float(input("Ingresa la cantidad a depositar: $"))
            depositar_dinero(cantidad)
            
        
        elif opcion == "3":
            cantidad = float(input("Ingresa la cantidad a retirar: $"))
            retirar_dinero(cantidad)

        elif opcion == "4":
            cuenta = input("Ingresa el numero de cuanta a transferir: ")
            cantidad = float(input("Ingresa la cantidad a transferir: $"))
            transferir_dinero(cuenta, cantidad)

        elif opcion == "5":
            ver_historial()
            
        elif opcion == "6":
            cambiar_pin()

        elif opcion == "7":
            login.cajero_acceso = False
            login.star_login()
        if opcion == "8":
            break