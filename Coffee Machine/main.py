# Variables initialization
quarter = 0
dime = 0
nickel = 0
pennie = 0
input_amount = 0
loss = 0

water = 1000
milk = 500
coffee = 150

latte_cost = 2
espresso_cost = 1.2
cappuccino_cost = 1.7
money = 10

choice = ''


# Function to handle the order
def order():
    global choice, quarter, dime, nickel, pennie, input_amount

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        print(f"Water: {water}")
        print(f"Milk: {milk}")
        print(f"Coffee: {coffee}")
        print(f"Money: ${money}")
    elif choice == "off":
        print("Turning off....")
        return
    else:
        quarter = int(input("How many quarters do you have?: ")) * 0.25
        dime = int(input("How many dimes do you have?: ")) * 0.10
        nickel = int(input("How many nickels do you have?: ")) * 0.05
        pennie = int(input("How many pennies do you have?: ")) * 0.01
        input_amount = quarter + dime + nickel + pennie
        transaction(choice)


# Function to handle the transaction
def transaction(choice):
    global water, milk, coffee, money, loss

    if choice == "latte" and input_amount >= latte_cost:
        if water >= 150 and milk >= 200 and coffee >= 10:
            water -= 150
            milk -= 200
            coffee -= 10
            loss = input_amount - latte_cost
            money += latte_cost
            print("Dispensed! Here's your coffee: ☕")
            print(f"Here's your change: ${loss:.2f}")
        else:
            print("Not enough resources!")

    elif choice == "espresso" and input_amount >= espresso_cost:
        if water >= 100 and coffee >= 7:
            water -= 100
            coffee -= 7
            loss = input_amount - espresso_cost
            money += espresso_cost
            print("Dispensed! Here's your coffee: ☕")
            print(f"Here's your change: ${loss:.2f}")
        else:
            print("Not enough resources!")

    elif choice == "cappuccino" and input_amount >= cappuccino_cost:
        if water >= 120 and milk >= 180 and coffee >= 8:
            water -= 120
            milk -= 180
            coffee -= 8
            loss = input_amount - cappuccino_cost
            money += cappuccino_cost
            print("Dispensed! Here's your coffee: ☕")
            print(f"Here's your change: ${loss:.2f}")
        else:
            print("Not enough resources!")

    else:
        print("Transaction unsuccessful! Not enough money or invalid choice.")
        print(input_amount)

while choice!="off":
    order()
