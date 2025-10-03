from cuentas import cuentas


cajero_acceso = False
usuario = ""
nombre = ""
saldo = 0
pin = ""
historial = []

def star_login():
    global cajero_acceso, usuario, nombre, saldo, pin, historial

    while True:
        print("*************")
        print("LOGIN 👥")
        print("*************")
        usuario = input("Ingresa tu numero de cuenta: ")

        if usuario in cuentas.keys():
            pin = input("Ingresa tu PIN: ")

            if cuentas[usuario]["pin"] == pin:
                print("Usario y contraseña correctas")
                nombre = cuentas[usuario]["nombre"]
                saldo = cuentas[usuario]["saldo"]
                historial = cuentas[usuario]["historial"]
                cajero_acceso = True
                break
            else:
                print("PIN incorrecto")
        else:
            print("Usuario incorrecto o no existe")


star_login()

if __name__ == '__main__':
    print(f"Hola, {nombre}. Bienvenido a tu cajero")
    print(f"Tu saldo es: ${saldo}")

    log = input("Login: ")

    if log == "1":
        login_running = True