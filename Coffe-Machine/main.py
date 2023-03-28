from coffe_data import MENU
from coffe_data import resources

def print_report(money):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"water: {water},\nmilk: {milk}, \ncoffee: {coffee}, \nmoney: ${money}")
        
def check_resources(choose):
    if choose == "espresso":
        if resources["water"] > MENU["espresso"]["ingredients"]["water"] and resources["coffee"] > MENU["espresso"]["ingredients"]["coffee"]:
            return True
    else: 
        for key in resources:
            if resources[key] > MENU[choose]["ingredients"][key]:
                return True

def discount(choose):
    if choose == "espresso":
        resources["water"] -= MENU[choose]["ingredients"]["water"]
        resources["coffee"] -= MENU[choose]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[choose]["ingredients"]["water"]
        resources["milk"] -= MENU[choose]["ingredients"]["milk"]
        resources["coffee"] -= MENU[choose]["ingredients"]["coffee"]


def calculate(choose, quarters, dimes, nickles, pennies):
    total = 0
    total = (quarters*0.25) + (dimes*0.10) + (nickles*0.05)  + (pennies*0.01)
    print(f"TOTAL = {total}")
    if total >= MENU[choose]["cost"]:
        print("Si te alcanza!")
        total = round(total - MENU[choose]["cost"])
        print(f"Here is your change: ${total} dollars")
        return True
    else:
        print("No te alcanza")

money = 0
turn_off = False
while not turn_off:

    choose = input("What would you like? (espresso/latte/cappuccino): ")

    if choose == "report":
        print_report(money)
    elif choose == "off":
        turn_off = True
    elif check_resources(choose):
        print("Enough resources")
        quater = float(input("Insert total of quarters: "))
        dime = float(input("Insert total of dimes: "))
        nickel = float(input("Insert total of nickels: "))
        pennie = float(input("Insert total of pennies: ")) 
        if calculate(choose, quater, dime, nickel, pennie):
            print(f"Here is your {choose}. Enjoy it!")
            money += MENU[choose]["cost"]
            discount(choose)
    else:
        print(f"No enough ingredients to make a {choose}")

