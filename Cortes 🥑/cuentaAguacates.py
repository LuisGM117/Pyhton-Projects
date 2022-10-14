import os

def clear():
     os.system('clear')


n = int(input("Ingrese la cantidad de cortes: "))

clear()

print(f"{n} CORTES 🥑")

current = 0
print("\n")


for i in range (1,n+1):
    print("**************************************************")

    kilos = int(input(f"Ingrese la cantidad de kilos del corte #" + str(i) + ": "))
    default = 30
    total_kilos = kilos - default
    precio = int(input(f"Ingrese el precio del corte #" + str(i) + ": "))
    total = total_kilos * precio
    print('\033[1A' + '\033[K', end='')
    print('\033[1A' + '\033[K', end='')
    print("Kg totales: " + str(total_kilos))
    print("Precio $" + str(precio))
    print(f"El total del corte #{i}:    {total_kilos}kg x ${precio} = ${total:,.2f}")

    print("**************************************************\n")

    current += total
print(f"EL TOTAL FINAL ES DE: ${current:,.2f} \n")

print("**************************************************\n")




