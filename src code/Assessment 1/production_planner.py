import math
from recipe_manager import RecipeManager

# Calculates the production plan based on available ingredients and recipes
class ProductionPlanner:
    def __init__(self, recipe_manager):
        self.recipe_manager = recipe_manager

    def calculate_production_plan(self):
        message = """Units for each Ingredient\n
        kilogram : flour, sugar, salt, sprinkles, butter, baking powder, icing sugar
        Litre : oil, vanilla, milk
        Units : egg\n
        """
        print(message)

        available_ingredients = {}
        for ingredient_name in self.recipe_manager.recipes['Chocolate Cake'].ingredients.keys():
            amount = float(input(f"Enter the amount of {ingredient_name} available: "))
            available_ingredients[ingredient_name] = amount

        max_cakes = {}
        for cake_name in self.recipe_manager.recipes.keys():
            max_cake = float('inf')
            for ingredient_name, amount_unit in self.recipe_manager.recipes[cake_name].ingredients.items():
                amount_required = amount_unit.amount
                if ingredient_name in available_ingredients:
                    amount_available = available_ingredients[ingredient_name]
                    max_cake = min(max_cake, amount_available // amount_required)
                else:
                    max_cake = 0
                    break

            # Round down the number of cakes to the nearest whole number
            max_cake = math.floor(max_cake)
            max_cakes[cake_name] = max_cake

        return max_cakes