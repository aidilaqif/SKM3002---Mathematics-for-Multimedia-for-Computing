from recipe import Recipe

# Manages recipes, allowing for addition and retrieval
class RecipeManager:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self, recipe):
        self.recipes[recipe.name] = recipe

    def get_recipe(self, name):
        return self.recipes.get(name)