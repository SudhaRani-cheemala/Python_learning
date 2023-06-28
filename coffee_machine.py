MENU={
"espresso":{
  "ingredents":{
        "water":50,
        "coffee":18
  },
  "cost":2.5
},
"latte":{
  "ingredents":{
        "water":50,
        "coffee":18,
        "milk":20
  },
   "cost":1.5,

},
"cappuccino":{
    "ingredients":{
        "water":20,
        "coffee":30,
        "milk":40
    },
 "cost":2.0
}
}
profit=0
resources={
  "milk":300,
   "water":200,
   "coffee":100, 
}
def is_resource_ingredients(order_ingfedients):
    """Returns True when the order can be made,False if ingredients are insufficient"""
    for item in order_ingfedients:
       if order_ingfedients[item]>=resources[item]:
           print("Sorry there is no enough water.")
           return False
    return True     
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins??")
    total=int(input("how many quarters?:"))*0.25
    total+=int(input("how many dimes?:"))*0.1
    total+=int(input("how many nickles?:"))*0.05
    total+=int(input("how many pennies?:"))*0.01
    return total
def is_transaction_successful(money_received,drink_cost):
    """Return True when the payment is accepted,or False if money is insufficient. """
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Here is ${change} in change")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money.Money refunded.")
        return False      
def make_coffee(drink_name,order_ingredents):
    for item in order_ingredents:
        resources[item]-=order_ingredents[item]
    print(f"Here is your {drink_name}")    

is_on=True
while is_on:
    choice=input("What would you like to drink?(espresso/cappuccino/latte):")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water:{resources['water']}ml")    
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}ml")
        print(f"Money:${profit}")
    else:
        drink=MENU[choice]    
        print(drink)
        if is_resource_ingredients(drink["ingredents"]):
           payment=process_coins()
           if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredents"]) 