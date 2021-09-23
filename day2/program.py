
meal_cost = float(input().strip())

tip_percent = int(input().strip())

tax_percent = int(input().strip())

def new_func(meal_cost, tip_percent, tax_percent):
    tip = (meal_cost * tip_percent) / 100
    tax = (meal_cost * tax_percent) / 100
    totalCost = int(round(meal_cost + tip + tax))
    print(totalCost)

new_func(meal_cost, tip_percent, tax_percent)

    