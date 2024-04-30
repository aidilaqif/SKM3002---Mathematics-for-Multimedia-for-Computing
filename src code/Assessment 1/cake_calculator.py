import math

class CakeRecipe:
    def __init__(self, name, flour, sugar, salt, sprinkles, oil, butter, egg, vanilla, baking_powder, icing_sugar, milk):
        self.name = name
        self.ingredients = {
            'flour': flour,
            'sugar': sugar,
            'salt': salt,
            'sprinkles': sprinkles,
            'oil': oil,
            'butter': butter,
            'egg': egg,
            'vanilla': vanilla,
            'baking powder': baking_powder,
            'icing sugar': icing_sugar,
            'milk': milk
        }

# Define the recipes for chocolate and red velvet cakes
chocolate_recipe = CakeRecipe("Chocolate Cake", 0.2, 0.15, 0.001, 0.005, 0.100, 0.100, 3, 0.001, 0.002, 0.010, 0.2)
red_velvet_recipe = CakeRecipe("Red Velvet Cake", 0.18, 0.12, 0.001, 0.005, 0.08, 0.08, 2, 0.001, 0.002, 0.010, 0.2)

message = """"
Units for each Ingredients\n
kilogram : flour, sugar, salt, sprinkles, butter, baking powder, icing sugar
Litre : oil, vanilla, milk
Units : egg\n
"""

def calculate_production_plan():
    print(message)
    available_ingredients = {}
    for ingredient in chocolate_recipe.ingredients.keys():
        amount = float(input(f"Enter the amount of {ingredient} available: "))
        available_ingredients[ingredient] = (amount)

    max_chocolate_cakes = float('inf')
    max_red_velvet_cakes = float('inf')

    # Calculate the maximum number of cakes for each type based on the available ingredients
    for cake in [chocolate_recipe, red_velvet_recipe]:
        max_cakes = float('inf')
        for ingredient, amount_unit in cake.ingredients.items():
            amount_required = amount_unit
            if ingredient in available_ingredients:
                amount_available = available_ingredients[ingredient]
                max_cakes = min(max_cakes, amount_available // amount_required)
            else:
                max_cakes = 0
                break

        # Round down the number of cakes to the nearest whole number
        max_cakes = math.floor(max_cakes)

        if cake.name == "Chocolate Cake":
            max_chocolate_cakes = max_cakes
        elif cake.name == "Red Velvet Cake":
            max_red_velvet_cakes = max_cakes

    return max_chocolate_cakes, max_red_velvet_cakes

max_chocolate_cakes, max_red_velvet_cakes = calculate_production_plan()

print(f"\nOptimum number of Chocolate Cakes: {max_chocolate_cakes}")
print(f"Optimum number of Red Velvet Cakes: {max_red_velvet_cakes}")