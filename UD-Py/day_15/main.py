from menu import MENU, resources


def starting_supply(supply):
    machine_water = supply["water"]
    machine_milk = supply["milk"]
    machine_coffee = supply["coffee"]
    return (f" Water remaining: {machine_water}\n"
            f" Milk remaining: {machine_milk}\n"
            f" Coffee remaining: {machine_coffee}")


machine_is_on = True
resources["money"] = 0
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
espresso_price = MENU["espresso"]["cost"]
latte_price = MENU["latte"]["cost"]
cappuccino_price = MENU["cappuccino"]["cost"]
print(f"Starting resources are as follows:\n{starting_supply(resources)}")

while machine_is_on:
    order_complete = False
    while not order_complete:
        choice = input("What would you like? (espresso/latte/cappuccino)\n").lower()
        if choice == "espresso":
            print(f"One {choice} coming right up!\n")
            if water < MENU["espresso"]["ingredients"]["water"]:
                print("Not enough water")
                break
            if coffee < MENU["espresso"]["ingredients"]["coffee"]:
                print("Not enough coffee")
                break
            else:
                print("insert coins please")
                quarters = float(input("How many quarters?: "))
                dimes = float(input("How many dimes?: "))
                nickels = float(input("How many nickles?: "))
                pennies = float(input("How many pennies?: "))
                total = round((0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies), 2)
                print(f"total coins inserted is ${total}\n")
                if total >= espresso_price:
                    change = round(total - espresso_price, 2)
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {choice}. enjoy!")
                    resources["money"] = resources["money"] + espresso_price
                    water = water - MENU["espresso"]["ingredients"]["water"]
                    coffee = coffee - MENU["espresso"]["ingredients"]["coffee"]
                elif total < espresso_price:
                    print("Sorry that's not enough money. Money refunded.")

        elif choice == "latte":
            print(f"One {choice} coming right up!\n")
            if water < MENU["latte"]["ingredients"]["water"]:
                print("Not enough water")
                break
            if milk < MENU["latte"]["ingredients"]["milk"]:
                print("Not enough milk")
                break
            if coffee < MENU["latte"]["ingredients"]["coffee"]:
                print("Not enough coffee")
                break
            else:
                print("insert coins please")
                quarters = float(input("How many quarters?: "))
                dimes = float(input("How many dimes?: "))
                nickels = float(input("How many nickles?: "))
                pennies = float(input("How many pennies?: "))
                total = round((0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies), 2)
                print(f"total coins inserted is ${total}")
                if total >= latte_price:
                    change = round(total - latte_price, 2)
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {choice}. enjoy!")
                    resources["money"] = resources["money"] + latte_price
                    water = water - MENU["latte"]["ingredients"]["water"]
                    coffee = coffee - MENU["latte"]["ingredients"]["coffee"]
                elif total < latte_price:
                    print("Sorry that's not enough money. Money refunded.")

        elif choice == "cappuccino":
            print(f"One {choice} coming right up!\n")
            if water < MENU["cappuccino"]["ingredients"]["water"]:
                print("Not enough water")
                break
            if milk < MENU["cappuccino"]["ingredients"]["milk"]:
                print("Not enough milk")
                break
            if coffee < MENU["cappuccino"]["ingredients"]["coffee"]:
                print("Not enough coffee")
                break
            else:
                print("insert coins please")
                quarters = float(input("How many quarters?: "))
                dimes = float(input("How many dimes?: "))
                nickels = float(input("How many nickles?: "))
                pennies = float(input("How many pennies?: "))
                total = round((0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies), 2)
                print(f"total coins inserted is ${total}\n")
                if total >= cappuccino_price:
                    change = round(total - cappuccino_price, 2)
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {choice}. enjoy!")
                    resources["money"] = resources["money"] + cappuccino_price
                    water = water - MENU["cappuccino"]["ingredients"]["water"]
                    milk = milk - MENU["cappuccino"]["ingredients"]["milk"]
                    coffee = coffee - MENU["cappuccino"]["ingredients"]["coffee"]
                elif total < cappuccino_price:
                    print("Sorry that's not enough money. Money refunded.\n")

        elif choice == "report":
            print(f"Water: {water}\n"
                  f"Milk: {milk}\n"
                  f"coffee: {coffee}\n"
                  f"money: ${resources['money']}\n")

        elif choice == "off":
            machine_is_on = False
            order_complete = True
            print("Goodbye!")

        else:
            print("Please enter a valid input\n")
