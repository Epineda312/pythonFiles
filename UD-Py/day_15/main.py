from menu import MENU, resources


def report(supply):
    machine_water = supply["water"]
    machine_milk = supply["milk"]
    machine_coffee = supply["coffee"]
    return (f" Water remaining: {machine_water}\n"
            f" Milk remaining: {machine_milk}\n"
            f" Coffee remaining: {machine_coffee}")


machine_is_on = True
espresso_price = MENU["espresso"]["cost"]
latte_price = MENU["latte"]["cost"]
cappuccino_price = MENU["cappuccino"]["cost"]

while machine_is_on:
    print(f"Starting resources are as follows:\n{report(resources)}")
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    order_complete = False
    while not order_complete:
        choice = input("What would you like? (espresso/latte/cappuccino)\n").lower()
        print(f"One {choice} coming right up!")
        if choice == "espresso":
            print(f"Making {choice}")
            if water < 50:
                print("Not enough water")
            if coffee < 18:
                print("Not enough coffee")
            else:
                print("insert coins please")
                quarters = float(input("How many quarters?: "))
                dimes = float(input("How many dimes?: "))
                nickels = float(input("How many nickles?: "))
                pennies = float(input("How many pennies?: "))
                total = ((0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies))
                if total >= espresso_price:
                    change = total - espresso_price
                    print(f"Here is ${round(change)} in change.")
                    print(f"Here is your {choice}. enjoy!")
                elif total < espresso_price:
                    print("Sorry that's not enough money. Money refunded.")

        elif choice == "latte":
            print(f"{choice}")
            if choice == "latte":
                print(f"Making {choice}")
                if water < 200:
                    print("Not enough water")
                if coffee < 24:
                    print("Not enough coffee")
                if milk > 150:
                    print("Not enough Milk")
                else:
                    print("insert coins please")
                    quarters = float(input("How many quarters?: "))
                    dimes = float(input("How many dimes?: "))
                    nickels = float(input("How many nickles?: "))
                    pennies = float(input("How many pennies?: "))
                    total = ((0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies))
                    if total >= latte_price:
                        change = total - latte_price
                        print(f"Here is ${round(change)} in change.")
                        print(f"Here is your {choice}. enjoy!")
                    elif total < latte_price:
                        print("Sorry that's not enough money. Money refunded.")

        elif choice == "cappuccino":
            print(f"{choice}")

        elif choice == "report":
            print(f"{report(resources)}")

        elif choice == "off":
            machine_is_on = False
            order_complete = True

        else:
            print("Please enter a valid input")
