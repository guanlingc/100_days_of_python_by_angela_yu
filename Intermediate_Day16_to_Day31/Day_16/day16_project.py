# Create OOP version of the coffee machine in day 15
# Things to do

from resources.menu import Menu
from resources.coffee_maker import CoffeeMaker
from resources.money_machine import MoneyMachine

def run_coffee_machine():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    machine_is_running = True

    while machine_is_running:
        coffee_choice = input(f"What would you like? {menu.get_items()}: ").lower()
        if coffee_choice == 'off':
            print(f"shutting down machine for maintenance")
            machine_is_running = False
        elif coffee_choice == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(coffee_choice) # use menu to get drink's attributes
            # print(drink.name,drink.cost,drink.ingredients)            
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
            else:
                print(f"Sorry, we don't serve {coffee_choice}.")
            
if __name__ == "__main__":
    run_coffee_machine()