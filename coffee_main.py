from coffee_menu import Menu,MenuItem
from coffeemaker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
coffeemaker=CoffeeMaker()
coffee_menu=Menu()
is_on=True

coffeemaker.report()
money_machine.report()

while is_on:
    options=coffee_menu.get_items()
    choice=input(f"What would you like?{options}")
    if choice=="report":
        is_on=False
    elif choice=="report":
        coffeemaker.report()
        money_machine.report()
    else:
        drink=coffee_menu.find_drink(choice)   
        if coffeemaker.is_resource_sufficient(drink) and   money_machine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)
          
                
    
    