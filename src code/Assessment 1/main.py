from unit import Unit
from ingredient import Ingredient
from recipe import Recipe
from recipe_manager import RecipeManager
from production_planner import ProductionPlanner

# Define the recipes for chocolate and red velvet cakes
recipe_manager = RecipeManager()
recipe_manager.add_recipe(Recipe("Chocolate Cake", {
    'flour': Ingredient('flour', 0.2, Unit.KILOGRAM),
    'sugar': Ingredient('sugar', 0.15, Unit.KILOGRAM),
    'salt': Ingredient('salt', 0.001, Unit.KILOGRAM),
    'sprinkles': Ingredient('sprinkles', 0.005, Unit.KILOGRAM),
    'oil': Ingredient('oil', 0.100, Unit.LITRE),
    'butter': Ingredient('butter', 0.100, Unit.KILOGRAM),
    'egg': Ingredient('egg', 3, Unit.UNIT),
    'vanilla': Ingredient('vanilla', 0.001, Unit.LITRE),
    'baking powder': Ingredient('baking powder', 0.002, Unit.KILOGRAM),
    'icing sugar': Ingredient('icing sugar', 0.010, Unit.KILOGRAM),
    'milk': Ingredient('milk', 0.2, Unit.LITRE)
}))
recipe_manager.add_recipe(Recipe("Red Velvet Cake", {
    'flour': Ingredient('flour', 0.18, Unit.KILOGRAM),
    'sugar': Ingredient('sugar', 0.12, Unit.KILOGRAM),
    'salt': Ingredient('salt', 0.001, Unit.KILOGRAM),
    'sprinkles': Ingredient('sprinkles', 0.005, Unit.KILOGRAM),
    'oil': Ingredient('oil', 0.08, Unit.LITRE),
    'butter': Ingredient('butter', 0.08, Unit.KILOGRAM),
    'egg': Ingredient('egg', 2, Unit.UNIT),
    'vanilla': Ingredient('vanilla', 0.001, Unit.LITRE),
    'baking powder': Ingredient('baking powder', 0.002, Unit.KILOGRAM),
    'icing sugar': Ingredient('icing sugar', 0.010, Unit.KILOGRAM),
    'milk': Ingredient('milk', 0.2, Unit.LITRE)
}))

planner = ProductionPlanner(recipe_manager)
max_cakes = planner.calculate_production_plan()

for cake_name, max_cake in max_cakes.items():
    print(f"\nOptimum number of {cake_name}: {max_cake}")
