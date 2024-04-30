from ingredient import Ingredient

# Represents a recipe with a name and a dictionary of ingredients
class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients