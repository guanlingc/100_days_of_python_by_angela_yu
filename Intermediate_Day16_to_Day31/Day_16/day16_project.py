# Create OOP version of the coffee machine in day 15
# Things to do

from resources.menu import Menu
from resources.coffee_maker import CoffeeMaker
from resources.money_machine import MoneyMachine

def run_coffee_machine():
    menu = Menu()
    machine_is_running = True

    while machine_is_running:
        coffee_choice = input(f"What would you like? {menu.get_items()}: ").lower()
        if coffee_choice == 'off':
            print(f"shutting down machine for maintenance")
            machine_is_running = False
        elif coffee_choice == 'report':
            coffee_maker = CoffeeMaker()
            coffee_maker.report()
        else:
            drink = menu.find_drink(coffee_choice) # use menu to get drink's attributes
            # print(drink.name,drink.cost,drink.ingredients)
            coffee_maker = CoffeeMaker()
            if coffee_maker.is_resource_sufficient(drink):
                money_machine = MoneyMachine()
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
                else:
                    pass
            else:
                pass
            
if __name__ == "__main__":
    run_coffee_machine()