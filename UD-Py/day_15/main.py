from menu import MENU, resources


def report(supply):
    machine_water = supply["water"]
    machine_milk = supply["milk"]
    machine_coffee = supply["coffee"]
    return (f" Water remaining: {machine_water}\n"
            f" Milk remaining: {machine_milk}\n"
            f" Coffee remaining: {machine_coffee}")


machine_is_on = True
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
espresso_price = MENU["espresso"]["cost"]
latte_price = MENU["latte"]["cost"]
cappuccino_price = MENU["cappuccino"]["cost"]
resources["money"] = 0

while machine_is_on:
    print(f"Starting resources are as follows:\n{report(resources)}")

    order_complete = False
    while not order_complete:
        choice = input("What would you like? (espresso/latte/cappuccino)\n").lower()
        print(f"One {choice} coming right up!")
        if choice == "espresso":
            print(f"Making {choice}")
            if water < MENU["espresso"]["ingredients"]["water"]:
                print("Not enough water")
            if coffee < MENU["espresso"]["ingredients"]["coffee"]:
                print("Not enough coffee")
            else:
                print("insert coins please")
                quarters = float(input("How many quarters?: "))
                dimes = float(input("How many dimes?: "))
                nickels = float(input("How many nickles?: "))
                pennies = float(input("How many pennies?: "))
                total = round((0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies), 2)
                print(f"total coins inserted is ${total}")
                if total >= espresso_price:
                    change = round(total - espresso_price, 2)
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {choice}. enjoy!")
                    resources["money"] = resources["money"] + espresso_price
                    print(f"Current money in the machine = ${resources['money']}")
                    water = water - MENU["espresso"]["ingredients"]["water"]
                    coffee = coffee - MENU["espresso"]["ingredients"]["coffee"]
                    print(f"After this drink, machine holds: {water} water and: {coffee} coffee")
                elif total < espresso_price:
                    print("Sorry that's not enough money. Money refunded.")

        elif choice == "latte":
            print(f"Making {choice}")
            if water < MENU["latte"]["ingredients"]["water"]:
                print("Not enough water")
            if milk < MENU["latte"]["ingredients"]["milk"]:
                print("Not enough milk")
            if coffee < MENU["latter"]["ingredients"]["coffee"]:
                print("Not enough coffee")
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
                    print(f"Current money in the machine = ${resources['money']}")
                    water = water - MENU["latte"]["ingredients"]["water"]
                    coffee = coffee - MENU["latte"]["ingredients"]["coffee"]
                    print(f"After this drink, machine holds: {water} water and: {coffee} coffee")
                elif total < latte_price:
                    print("Sorry that's not enough money. Money refunded.")

        elif choice == "cappuccino":
            print(f"Making {choice}")
            if water < MENU["cappuccino"]["ingredients"]["water"]:
                print("Not enough water")
            if milk < MENU["cappuccino"]["ingredients"]["milk"]:
                print("Not enough milk")
            if coffee < MENU["cappuccino"]["ingredients"]["coffee"]:
                print("Not enough coffee")
            else:
                print("insert coins please")
                quarters = float(input("How many quarters?: "))
                dimes = float(input("How many dimes?: "))
                nickels = float(input("How many nickles?: "))
                pennies = float(input("How many pennies?: "))
                total = round((0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies), 2)
                print(f"total coins inserted is ${total}")
                if total >= cappuccino_price:
                    change = round(total - cappuccino_price, 2)
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {choice}. enjoy!")
                    resources["money"] = resources["money"] + cappuccino_price
                    print(f"Current money in the machine = ${resources['money']}")
                    water = water - MENU["cappuccino"]["ingredients"]["water"]
                    coffee = coffee - MENU["cappuccino"]["ingredients"]["coffee"]
                    print(f"After this drink, machine holds: {water} water and: {coffee} coffee")
                elif total < cappuccino_price:
                    print("Sorry that's not enough money. Money refunded.")

        elif choice == "report":
            print(f"{report(resources)}")

        elif choice == "off":
            machine_is_on = False
            order_complete = True
            print("Goodbye!")

        else:
            print("Please enter a valid input")
