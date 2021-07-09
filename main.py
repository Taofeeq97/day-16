MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit=0
resources={
    "water":300,
    "milk": 200,
    "coffee": 100
}

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coin():
    print("print input your coin")
    total=int(input("how many penny do you have?")) *0.01
    total+= int(input("how many dime do you have?"))* 0.1
    total+= int(input("how many nickel do you have?"))*0.05
    total+= int(input("how many quarter do you have?"))*0.25
    return total


def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved>= drink_cost:
        change= round(money_recieved-drink_cost)
        print(f"here is ${change} change")
        global profit
        profit+= drink_cost
        return True
    else:
        print("sorry there is not enough money, you will be refunded")
        return False


def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item]-= order_ingredient[item]
    print(f"here is your {drink_name} enjoy")


end_of_order=False
while not end_of_order:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice=="off":
        end_of_order=True
    elif choice== "report":
        print(f"water is {resources['water']} ml")
        print(f"milk is {resources['milk']} ml")
        print(f"coffee is {resources['coffee']} ml")
        print(f" money is $:{profit} ")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])