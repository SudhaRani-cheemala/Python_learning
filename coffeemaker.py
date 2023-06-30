class CoffeeMaker:
    def __init__(self):
        self.resources={
            "water":300,
            "milk":200,
            "coffee":100,
        }
    def report(self):
        print(f"Water:{self.resources['water']}ml")
        print(f"Milk:{self.resources['milk']}ml")
        print(f"Coffee:{self.resources['coffee']}ml")
    def is_resource_sufficient(self,drink):
        can_make=True
        for item in drink.ingredients:
            if drink.ingredients[item]>self.resources[item]:
                print("Sorry there is not enough{item}")   

    

    


    