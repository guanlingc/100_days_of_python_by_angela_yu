from resource.day_15_coffee import MENU
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# tracks ingredients
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    }

# tracks the money
funds = 0




# Print report function
def print_report(resources_dict, current_credits):
    # Takes resources list and formats it for printing
    print(f"Water: {resources_dict['water']}ml \n"
          f"Milk: {resources_dict['milk']}ml \n"
          f"Coffee: {resources_dict['coffee']}g \n"
          f"Money: ${current_credits} \n")

# Check if resources are sufficient
def check_sources(resource,drink):
    # loop through each ingredient and compare value
    insufficient_ingredients = []
    for key, value in drink.items():
        if resource[key] < value:
            insufficient_ingredients.append(key)
            print(f"Sorry, there is not enough {key}")
    print(f'Your drink is available')
    return insufficient_ingredients #returns list if there is lacking ingredients

# check funds
def insert_coins():
    pennies = int(input(f"Insert pennies: "))
    nickles = int(input(f"Insert nickles: "))
    dimes = int(input(f"Insert dimes: "))
    quarters = int(input(f"Insert quarters: "))
    print(f"You have inserted {pennies} pennies, {nickles} nickles, {dimes} dimes, {quarters} quarters")
    return pennies, nickles, dimes, quarters

# calculate coin values
def check_coin_value(client_pennies, client_nickles, client_dimes, client_quarters):
    client_pennies = round((client_pennies * 0.01), 2)
    client_nickles = round((client_nickles * 0.05),2)
    client_dimes = round((client_dimes * 0.1),2)
    client_quarters = round((client_quarters * 0.25),2)
    total = client_pennies+ client_nickles + client_dimes + client_quarters
    print(f"That is a total of ${round(total,2)}")
    return total

def make_coffee(resources:dict, coffee_ingredients:dict):
    for key,value in resources.items():
        if key in coffee_ingredients:
            resources[key] -= coffee_ingredients[key]


#Start Machine
machine_in_operation = True
# List of available drinks
available_drinks = ['espresso','latte','cappuccino']

while machine_in_operation:
    coffee_choice = input(f"What would you like? (espresso/latte/cappuccino): ").lower()

    # when off is entered into prompt its stops
    if coffee_choice == 'off':
        print(f"shutting down machine for maintenance")
        machine_in_operation = False
    elif coffee_choice == 'report':
        print(f"printing report")
        print_report(resources, funds)
    elif coffee_choice in available_drinks:
            chosen_drink_ingredients = MENU[coffee_choice]['ingredients']
            
            missing_ingredients = check_sources(resources, chosen_drink_ingredients)
            if not missing_ingredients:
                pennies, nickles, dimes, quarters = insert_coins()
                coin_value = check_coin_value(pennies, nickles, dimes, quarters)
                chosen_drink_cost = MENU[coffee_choice]['cost']
                if coin_value > chosen_drink_cost:
                    coin_value -= chosen_drink_cost
                    print(f"The {coffee_choice} cost ${chosen_drink_cost}")
                    print(f"I will return you a change of ${round(coin_value, 2)}")
                    make_coffee(resources,chosen_drink_ingredients)
                    funds += chosen_drink_cost
                    print(f"Here is your {coffee_choice}. Enjoy!")
                    print(f"\n" *5)
                else:
                    print(f"Sorry that's not enough money. Money refunded")
    else:
        print(f"Your choice is not available. Please try again")

